import json

from flask import Flask, request, jsonify, make_response, Response

from db.db import Database, Product

app = Flask(__name__)
database = Database()


@app.get('/products')
def products():  # put application's code here
    product_id = request.args.get('id')
    name = request.args.get('name')
    return_products = database.get_products(product_id=product_id, product_name=name)
    return Response(json.dumps(return_products), mimetype='application/json')


@app.get('/product')
def product():  # put application's code here
    product_id = request.args.get('id')
    name = request.args.get('name')
    return database.get_product(product_id=product_id, product_name=name).to_dict()


@app.post('/product/<id>')
def update_product(id):  # put application's code here
    product_id = request.args.get('id')
    product_name = request.args.get('name')
    product_price = request.args.get('price')
    updated_product = Product(product_id, product_name, product_price)
    database.update_product(id, updated_product)
    return "", 204


@app.post('/product')
def insert_product():  # put application's code here
    request_data = request.get_json()
    product_id = request_data['id']
    product_name = request_data['name']
    product_price = request_data['price']
    product = Product(product_id, product_name, product_price)
    database.insert_product(product)
    return "", 204


if __name__ == '__main__':
    app.run()
