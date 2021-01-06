import os
import sqlite3
from pathlib import Path

from flask import Flask

ROOT_DIR = str(Path(os.path.dirname(__file__)).parent)
DATABASE = ROOT_DIR + '/db/database.db'
SCHEMA = ROOT_DIR + '/db/schema.sql'

app = Flask(__name__)
g = {'_database': None}


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        print('Opening DB:' + DATABASE)
        db = g['_database'] = sqlite3.connect(DATABASE)
    return db


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource(SCHEMA, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def hello():
    return 'Welcome to Payment REST API from <b>Bank of Hong Kong Luna</b>'


@app.route('/payment/<id>')
def get_payment(id: int):

    cur = get_db().execute('SELECT * FROM payments WHERE id = ?', [id])
    rv = cur.fetchall()
    cur.close()

    if len(rv) == 1:
        return {
            'id': rv[0][0],
            'userId': rv[0][1],
            'iban': rv[0][2],
            'amount': rv[0][3],
            'reference': rv[0][4],
            'createdDate': rv[0][5]
        }
    else:
        return {'Error': "Payment with a given ID '%s' does not exist" % id}, 404
