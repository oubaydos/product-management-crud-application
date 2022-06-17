from flask import Flask

from db.db import db

app = Flask(__name__)


@app.get('/')
def hello_world():  # put application's code here
    db().get_product("1")
    return "hello"


if __name__ == '__main__':
    app.run()
