from flask import Flask, render_template
import sqlite3
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_cat(cat_id):
    conn = get_db_connection()
    cat = conn.execute('SELECT * FROM categories WHERE id = ?',
                        (cat_id,)).fetchone()
    conn.close()
    if cat is None:
        abort(404)
    return cat

def get_category_apis(cat_id):
    conn = get_db_connection()
    apis = conn.execute('SELECT * FROM products WHERE category = ?', (cat_id,)).fetchall()
    conn.close()
    if apis is None:
        abort(404)
    return apis


def get_api_data(link):
    pass



app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    conn.close()
    return render_template('index.html', categories = categories)



@app.route('/<cat_id>')
def cat(cat_id):
    cat = get_cat(cat_id)
    category_apis = get_category_apis(cat_id)
    return render_template('category.html', category = cat, apis = category_apis)


@app.route('/about')
def about():
    return render_template('about.html',)