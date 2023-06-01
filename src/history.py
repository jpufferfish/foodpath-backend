# https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb
#!/usr/bin/python
from __main__ import app
from flask import Flask, request, jsonify
from flask_jwt_extended import jwt_required
from datetime import datetime, timedelta
from enum import Enum
import pandas as pd
import sqlite3, csv

# CORS(app, resources={r"/*": {"origins": "*"}})

input_csv = '../data/input.csv'
input_fin_csv = '../data/inputfin.csv'

# super messy but no time
# only adding a SINGULAR FOOD, so dont even need to POST the whole seqrch query reponse from fdc
def insert_into_csv(mealtype, description, nutrients):
    for nutrient in nutrients:
        if nutrient['nutrientName'] == 'Energy':
            energy = nutrient['value'] if nutrient['unitName'] == 'kcal' else nutrient['value']*4.184
        elif nutrient['nutrientName'] == 'Protein':
            protein = nutrient['value'] if nutrient['unitName'] == 'g' else nutrient['value']*1000
        elif nutrient['nutrientName'] == 'Total lipid (fat)':
            fat = nutrient['value'] if nutrient['unitName'] == 'mg' else nutrient['value']/1000
        elif nutrient['nutrientName'] == 'Carbohydrate, by difference':
            carbs = nutrient['value'] if nutrient['unitName'] == 'mg' else nutrient['value']/1000
        elif nutrient['nutrientName'] == 'Fiber, total dietary':
            fiber = nutrient['value'] if nutrient['unitName'] == 'mg' else nutrient['value']/1000
        elif nutrient['nutrientName'] == 'Sugars, total':
            sugars = nutrient['value'] if nutrient['unitName'] == 'mg' else nutrient['value']/1000
        elif nutrient['nutrientName'] == 'Calcium, Ca':
            calcium = nutrient['value'] if nutrient['unitName'] == 'mg' else nutrient['value']/1000
        elif nutrient['nutrientName'] == 'Iron, Fe':
            iron = nutrient['value'] if nutrient['unitName'] == 'mg' else nutrient['value']/1000
        elif nutrient['nutrientName'] == 'Potassium, K':
            potassium = nutrient['value'] if nutrient['unitName'] == 'mg' else nutrient['value']/1000
        elif nutrient['nutrientName'] == 'Sodium, Na':
            sodium = nutrient['value'] if nutrient['unitName'] == 'mg' else nutrient['value']/1000
        elif nutrient['nutrientName'] == 'Vitamin D (D2 + D3)':
            vitaminD = nutrient['value'] if nutrient['unitName'] == 'mcg' else nutrient['value']/1000
    with open(input_csv, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([description, 1 if mealtype==0 else 0, 1 if mealtype==1 else 0, 1 if mealtype==2 else 0, 0,
                            energy, fat, protein, iron, calcium, sodium, potassium, carbs, fiber, vitaminD, sugars])
    with open(input_fin_csv, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(energy, fat, protein, iron, calcium, sodium, potassium, carbs, fiber, vitaminD, sugars)
    remove_csv_duplicate_rows(input_csv)
    remove_csv_duplicate_rows(input_fin_csv)
    return

def remove_csv_duplicate_rows(filename):
    df = pd.read_csv(filename)
    pd.drop_duplicates(inplace=True)   
    pd.to_csv(filename, index=False)

# https://charlesleifer.com/blog/going-fast-with-sqlite-and-python/
def connect_to_db():
    conn = sqlite3.connect('../data/database.db', timeout=10, isolation_level=None)
    conn.execute('pragma journal_mode=wal')
    return conn

# realistically should only return all logs of a specific username, not all logs of all usernames
# https://stackoverflow.com/questions/11285305/how-to-create-nested-tables-in-sqlite-database-android
# https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-and-sqlite
# https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-a-database
def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute()
        conn.commit()
        print("log table created successfully")
    except:
        print("log table creation failed - Maybe table")
    finally:
        conn.close()

# cur.execute("INSERT INTO lists (title) VALUES (?)", ('Work',))
# cur.execute("INSERT INTO items (list_id, content) VALUES (?, ?)", (1, 'Morning meeting'))
def insert_log(username, log, nutrients):
    try:
        create_db_table()
        conn = connect_to_db()
        cur = conn.cursor()
        # cur.execute('INSERT IGNORE INTO table logs (username, timestamp, food, mealtype) VALUES (?)', 
        #             (log['username'],))
        # cur.execute("INSERT INTO logs (entry_time, food, username) VALUES (?, ?, ?)"
        #             , (username, food_string) )
        cur.execute("INSERT INTO history (timestamp, food, mealtype, username) VALUES (?, ?, ?, ?)", \
                                     (datetime.now()-timedelta(days=4), log['food'], log['mealtype'], username))
        conn.commit()
        insert_into_csv(log['mealtype'], nutrients)
    except:
        conn().rollback()
    finally:
        conn.close()

# currently all user's logs
@app.route('/history/history', methods=['GET'])
def get_history():
    history = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM history")
        rows = cur.fetchall()
        # convert row objects to dictionary
        for i in rows:
            user = {}
            user["username"] = i["username"]
            users.append(user)
    except:
        print('EMPTY logs')
        users = []
    return users

# QUERY PARAMS, so for example: /logs?username=ted&mealtype=0&nutrients=...
# https://tedboy.github.io/flask/generated/generated/flask.Request.get_json.html
@app.route('/history/add',  methods = ['POST'])
# @jwt_required()
def api_add_log():
    args = request.args
    print('LOG ARGS: ', str(args))
    log = args.get('log')
    username = log.get('username')
    # mealtype = log.get('mealtype')
    nutrients = args.get_json('nutrients')
    return jsonify(insert_log(username, log, nutrients))

@app.route('/csv/clear')
# @jwt_required()
def api_clear_csv():
    return

# def 
#     switch(key){
#         case 203 : return 'Protein';
#         case 204 : return 'Fat';
#         case 205 : return 'Carbohydrate';
#         case 208 : return 'Energy';
#         case 268 : return 'Energy';
#         case 269 : return 'Sugars';
#         case 291 : return 'Fiber, total dietary';
#         case 301 : return 'Calcium';
#         case 303 : return 'Iron';
#         case 306 : return 'Potassium';
#         case 307 : return 'Sodium';
#         case 324 : return 'Vitamin D';
#         default : return 'Unknown';
#     }

# }