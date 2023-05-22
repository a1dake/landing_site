import os
import sys
import sqlite3

currentdir = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.join(currentdir, "goods.db")
sys.path.append(db_path)

def search_data():
    with sqlite3.connect(db_path) as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM goods")
        rows = cursor.fetchall()

        column_names = [description[0] for description in cursor.description]

        result = []
        for row in rows:
            row_dict = dict(zip(column_names, row))
            result.append(row_dict)
        return result