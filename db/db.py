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
                cursor.execute("SELECT * FROM PRODUCT WHERE product_id %% %s ORDER BY PRODUCT_NAME ASC", [product_id])
                return Product.from_tuple(cursor.fetchone())
            if product_name is not None:
                cursor.execute("SELECT * FROM PRODUCT WHERE product_name %% %s ORDER BY PRODUCT_NAME ASC; ", [product_name])
                return Product.from_tuple(cursor.fetchone())
            return Product.not_found()

    def update_product(self, product_id, product: Product):
        with self.connection.cursor() as cursor:
            if product_id is not None and product.product_name is not None:
                cursor.execute(
                    "UPDATE PRODUCT SET product_name= %s WHERE product_id = %s;",
                    [product.product_name, product_id])
                self.connection.commit()
            if product_id is not None and product.product_price is not None:
                cursor.execute(
                    "UPDATE PRODUCT SET product_price= %s WHERE product_id = %s",
                    [product.product_price, product_id])
                self.connection.commit()
            if product_id is not None and product.product_id is not None:
                cursor.execute(
                    "UPDATE PRODUCT SET product_id= %s WHERE product_id = %s;",
                    [product.product_id, product_id])
                self.connection.commit()

    def insert_product(self, product: Product):
        if None in product.to_dict().values():
            raise RuntimeError("cannot perform the action, product not complete")
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO PRODUCT VALUES(%s,%s,%s)",
                [product.product_id, product.product_name, product.product_price]
            )
            self.connection.commit()

    def get_products(self, product_id=None, product_name=None):
        L = []
        with self.connection.cursor() as cursor:
            if product_id is not None and product_id != "":
                cursor.execute(
                    "SELECT * FROM PRODUCT WHERE PRODUCT_ID %% %s ORDER BY PRODUCT_NAME ASC", [product_id]
                )
                temp = cursor.fetchall()
                for i in temp:
                    L.append(Product.from_tuple(i).to_dict())
            elif product_name is not None and product_name != "":
                cursor.execute(
                    "SELECT * FROM PRODUCT WHERE PRODUCT_NAME %% %s ORDER BY PRODUCT_NAME ASC", [product_name]
                )
                temp = cursor.fetchall()
                for i in temp:
                    L.append(Product.from_tuple(i).to_dict())
            else:
                cursor.execute(
                    "SELECT * FROM PRODUCT ORDER BY PRODUCT_NAME ASC"
                )
                temp = cursor.fetchall()
                for i in temp:
                    L.append(Product.from_tuple(i).to_dict())
        return L

    def delete_product(self, product_id):
        with self.connection.cursor() as cursor:
            if product_id is not None and product_id != "":
                cursor.execute(
                    "DELETE FROM PRODUCT WHERE PRODUCT_ID = %s", [product_id]
                )
