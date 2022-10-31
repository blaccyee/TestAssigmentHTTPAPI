from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.config import DATABASE_URL


def main():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())

    session.execute('''CREATE TABLE PRODUCTS (
                       ID INTEGER NOT NULL PRIMARY KEY,
                       NAME VARCHAR(256) );
    ''')

    session.execute('''CREATE TABLE CATEGORIES (
                       ID INTEGER NOT NULL PRIMARY KEY,
                       NAME VARCHAR(256) );
    ''')

    session.execute('''CREATE TABLE STORE (
                       ID INTEGER NOT NULL PRIMARY KEY,
                       CATEGORY_ID INTEGER,
                       PRODUCT_ID INTEGER );
    ''')

    session.close()


if __name__ == '__main__':
    main()
