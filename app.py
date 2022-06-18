from flask import Flask, request

from db.db import Database

app = Flask(__name__)
database = Database()


@app.get('/product')
def hello_world():  # put application's code here
    id = request.args.get('id')
    name = request.args.get('name')
    return database.get_product(product_id=id, product_name=name).to_dict()


if __name__ == '__main__':
    app.run()
