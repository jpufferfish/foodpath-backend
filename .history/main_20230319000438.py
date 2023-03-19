from flask import Flask, request, render_template,jsonify
from flask_cors import CORS
from threading import Thread
import sqlite3
import sys
import os

# Init. flask
app = Flask('')
# Cross origin 
CORS(app)
os.environ['TZ'] = ('US/EASTERN')
# Init. sql
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
    
# POST
@app.route('/create/', methods=('GET', 'POST'), strict_slashes=False)
def create():
    args = request.args.get('username')
    print(args, file=sys.stderr)
    if request.method == 'POST':
        data = request.get_json()
        print(data, file=sys.stderr)
        exercise = ''
        weight = ''
        total_weight=0
        repititions = ''
        worktime = ''
        for x in data:
          if x["username"] == None:
            username = 'null'
          else: 
            username = x["username"]

          if x['exercise'] == None:
            exercise = 'null,' + exercise
          else: 
            exercise = x['exercise']  + "," + exercise

          if x['weight'] == None:
            weight = 'null,' + weight
          else: 
            weight = x['weight'] + "," + (str(weight))
          
          if type(x['totalWeight']) == type(100):
            if x['totalWeight'] > total_weight:
              total_weight = x['totalWeight']
          
          if x['repitions'] == None:
              repititions = 'null,' + repititions
          else: 
            repititions = x['repitions'] + "," + repititions

          worktime = x['time'] + "," + worktime
          created = x['created']
        conn = get_db_connection()
        workouts = conn.execute('SELECT * FROM workouts WHERE username = ? And created = ?', (args,created)).fetchall()
      
        is_present = bool(workouts)
        if is_present:
            print("Previous workout flag being returned", file=sys.stderr)
            conn.close()
            return "ALREADY logged" 
        conn.execute(
          'INSERT INTO workouts (username, exercise, weight,repititions,totalweight, time, created ) VALUES (?,?,?,?,?,?,?)',
          (username, exercise, weight, repititions, total_weight, worktime, created, ))
        conn.commit()
        conn.close()
        
    return "POSTED!"

# GET (WEB)
@app.route('/')
def index():
    conn = get_db_connection()
    workouts = conn.execute('SELECT * FROM workouts').fetchall()
    conn.close()
    return render_template('webIndex.html', workouts=workouts)

# TODO: GET method for all(MOBILE) rather than specific workouts


# GET (MOBILE apps)
@app.route('/api/', methods=["GET"], strict_slashes=False)
def GET():
    username = request.args.get('username')
    userDate =request.args.get('date')
    print(username, file=sys.stderr)
    print(userDate, file=sys.stderr)
    conn = get_db_connection()
    workouts = conn.execute('SELECT * FROM workouts WHERE username = ? And created = ?',(username,userDate)).fetchall()
    conn.close()
    large ={}
    i = 0
    for x in workouts:
      small ={}
      small['exercise'] = str(x['exercise'])
      small['weight'] = str(x['weight'])
      small['totalweight'] = x['totalweight']
      small['repititions'] = x['repititions']
      small ['time'] = x['time']
      small ['created'] = x['created']
      large[i] = small 
      i = i+1

    has_items = bool(large)
    if has_items:
      print(large, file=sys.stderr)
      return jsonify(large)
    else:
      small ={}
      small['exercise'] = "null"
      small['weight'] ="null"
      small['repititions'] = "null"
      small ['time'] = "null"
      small ['created'] = "null"
      large[0] = small
      print("NULL", file=sys.stderr)
      return jsonify(large)
# RUN
def run():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=7000)

t = Thread(target=run)
t.start()
