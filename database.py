
"""
    This file contains the Databse Class
    Database consists of 2 Tables
    1. categories: It consist of list of all the scrapped categories
    SCHEMA:
        || id | category_name ||

    2. products: It consist the list of all the APIs
    SCHEMA:
        ||prod_id | category(id) | apiName | Link ||
        (Other Data not scrapped as mentioned in Assignment) 


"""




import sqlite3

class Database():
    
    # CONSTRUCTOR TO INITIATE A NEW DATABSE WITH FORMED SCHEMA
    def __init__(self,name):
        self.connection = sqlite3.connect(name)
        with open('schema.sql') as f:
            self.connection.executescript(f.read())

    # FUNCTION TO SAVE THE LIST OF CATEGORIES
    def save_categories(self,category_list):
        cur = self.connection.cursor()
        for cat in category_list:
            cur.execute("INSERT INTO categories (category_name) VALUES (?)", (cat,))
        self.connection.commit()
        categories = cur.execute('SELECT * FROM categories').fetchall()
        return categories

    # FUNCTION TO SAVE AN API IN DB
    def saveApi(self, id, API, Link):
        cur = self.connection.cursor()
        cur.execute("INSERT INTO products(category, apiName, link) VALUES (?,?,?)", (id,API, Link))
        self.connection.commit()
    
    # DESTRUCTOR TO CLOSE THE DB CONNECTION
    def __del__(self):
        self.connection.close()
