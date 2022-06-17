import logging

from db.init import init
from logs.logger import logger


class db:
    connection = None

    def __init__(self):
        self.connection = init()

    def get_product(self, product_id = None, product_name = None):
        with self.connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM PRODUCT ")
            logger.info(cursor.fetchall())
            return
            if product_id is None:
                return cursor.execute(f"SELECT * FROM PRODUCT WHERE product_id = {product_id} ")
            return cursor.execute(f"SELECT * FROM PRODUCT WHERE product_name = {product_name} ")
