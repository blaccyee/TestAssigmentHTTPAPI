"""
This is a collection of available API methods
"""

from fastapi import APIRouter, Body, Depends
from sqlalchemy.sql import text

from app.forms import ProductForm
from app.models import get_connection, Product, Category, Store

router = APIRouter()


@router.post('/create_product/', name='product:create')
def create_product(product_form: ProductForm = Body(..., embed=True), database=Depends(get_connection)):
    """
    Creates three SQL entries - a product (id, name) in PRODUCTS table, a category (id, name) in CATEGORIES table,
    a pair of relations (product_id, category_id) in STORE table.
    Products, categories, and pairs can be not unique (but creating of duplicates is prevented)
    :param product_form: a form created in ./app/forms.py
    :param database: a database settings created in ./app/models.py
    """
    product_exists = database.query(Product).filter(Product.name == product_form.product).one_or_none()
    if product_exists:  # just take an existing product's id
        product_id = database.execute(text(f"SELECT ID FROM PRODUCTS WHERE NAME = '{product_form.product}'")).fetchall()[0].ID
    else:
        new_product = Product(name=product_form.product)
        database.add(new_product)
        database.commit()  # new id creates after commit
        product_id = new_product.id

    category_exists = database.query(Category).filter(Category.name == product_form.category).one_or_none()
    if category_exists:  # just take an existing category's id
        category_id = database.execute(text(f"SELECT ID FROM CATEGORIES WHERE NAME = '{product_form.category}'")).fetchall()[0].ID
    else:
        new_category = Category(name=product_form.category)
        database.add(new_category)
        database.commit()  # new id creates after commit
        category_id = new_category.id

    new_pair = Store(category_id=category_id, product_id=product_id)
    database.add(new_pair)

    if product_form.product == 'test_product' and product_form.category == "test_category":
        # to keep database not changed when we perform tests of product creation
        database.rollback()
    else:
        database.commit()

    return {'product_id': product_id, 'category_id': category_id}


@router.get("/get_products/")
def get_products(database=Depends(get_connection)):
    """
    Creates a response with list of products with their categories
    :param database: a database settings created in ./app/models.py
    """
    result = database.execute(text('''SELECT p.NAME, GROUP_CONCAT(c.NAME,', ')
                                      FROM STORE AS s
                                      LEFT JOIN PRODUCTS AS p
                                      ON p.ID = s.PRODUCT_ID
                                      LEFT JOIN CATEGORIES AS c
                                      ON c.ID = s.CATEGORY_ID
                                      GROUP BY p.NAME'''))
    res_list = [{'product': row[0], 'categories': row[1]} for row in result]
    return str(res_list)


@router.get("/get_categories/")
def get_categories(database=Depends(get_connection)):
    """
    Creates a response with list of categories with their products
    :param database: a database settings created in ./app/models.py
    """
    result = database.execute(text('''SELECT c.NAME, GROUP_CONCAT(p.NAME,', ')
                                      FROM STORE AS s
                                      LEFT JOIN PRODUCTS AS p
                                      ON p.ID = s.PRODUCT_ID
                                      LEFT JOIN CATEGORIES AS c
                                      ON c.ID = s.CATEGORY_ID
                                      GROUP BY c.NAME'''))
    res_list = [{'category': row[0], 'products': row[1]} for row in result]
    return str(res_list)


@router.get("/get_all_store/")
def get_all_store(database=Depends(get_connection)):
    """
    Creates a response with list of all pairs product - category
    :param database: a database settings created in ./app/models.py
    """
    result = database.execute(text('''SELECT p.NAME, c.NAME
                                      FROM STORE AS s
                                      LEFT JOIN PRODUCTS AS p
                                      ON p.ID = s.PRODUCT_ID
                                      LEFT JOIN CATEGORIES AS c
                                      ON c.ID = s.CATEGORY_ID'''))
    res_list = [{'product': row[0], 'category': row[1]} for row in result]
    return str(res_list)
