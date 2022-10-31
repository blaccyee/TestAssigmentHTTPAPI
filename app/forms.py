"""
A simple form for our API application
Example:
    {
        "product_form": {
            "product": "string",
            "category": "string"
        }
    }
"""

from pydantic import BaseModel


class ProductForm(BaseModel):
    product: str
    category: str
