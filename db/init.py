import logging

import psycopg2

from logs.logger import logger


def init(host="localhost", database="baba", user="nephojar", password="nephojar"):
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    logger.debug("Opened database successfully")
    cur = conn.cursor()
    query = f'''CREATE TABLE IF NOT EXISTS PRODUCT(
                        product_id varchar(30) PRIMARY KEY NOT NULL,
                        product_name varchar(30) NOT NULL UNIQUE,
                        product_price real NOT NULL)'''
    cur.execute(query)
    conn.commit()
    cur.close()
    logger.debug("created the db")
    return conn
