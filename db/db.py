import logging

from db.init import init
from logs.logger import logger


class Product:
    product_id = None
    product_name = None
    product_price = None

    def __init__(self, product_id, product_name, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price

    @classmethod
    def from_tuple(cls, product_tuple: tuple):
        if product_tuple is None:
            return cls.not_found()
        return cls(product_tuple[0], product_tuple[1], product_tuple[2])

    def to_dict(self) -> dict:
        return {"product_id": self.product_id, "product_name": self.product_name, "product_price": self.product_price}

    @classmethod
    def not_found(cls):
        return cls("0", "product not found", 0)


class Database:
    connection = None

    def __init__(self):
        self.connection = init()

    def get_product(self, product_id=None, product_name=None) -> Product:
        with self.connection.cursor() as cursor:
            if product_id is not None:
                cursor.execute("SELECT * FROM PRODUCT WHERE product_id = %s ", [product_id])
                return Product.from_tuple(cursor.fetchone())
            if product_name is not None:
                cursor.execute("SELECT * FROM PRODUCT WHERE product_name = %s ", [product_name])
                return Product.from_tuple(cursor.fetchone())
            return Product.not_found()
