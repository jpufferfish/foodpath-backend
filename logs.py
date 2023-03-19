# https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb
#!/usr/bin/python
import sqlite3
from flask import Flask, request, jsonify #added to top of file
from flask_cors import CORS #added to top of file
# app = Flask(__name__)
from __main__ import app
CORS(app, resources={r"/*": {"origins": "*"}})

def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn

def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute( '''CREATE TABLE IF NOT EXISTS logs (
          log_id INTEGER PRIMARY KEY NOT NULL, 
          username TEXT, 
          entry_time DATETIME, 
          food TEXT);'''
        )
        conn.commit()
        print("log table created successfully")
    except:
        print("log table creation failed - Maybe table")
    finally:
        conn.close()

def insert_log(log):
    inserted_log = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO logs (username, entry_time, food) VALUES (?, ?, ?)"
                    , (log['username'], log['entry_time'], log['food']) )
        conn.commit()
        inserted_log = get_log_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_log

def get_logs():
    logs = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM logs")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            log = {}
            log["log_id"] = i["log_id"]
            log["username"] = i["username"]
            log["entry_time"] = i["entry_time"]
            log["food"] = i["food"]
            logs.append(log)

    except:
        logs = []

    return logs


def get_log_by_id(log_id):
    log = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM logs WHERE log_id = ?", 
                       (log_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        log["log_id"] = row["log_id"]
        log["username"] = row["username"]
        log["entry_time"] = row["entry_time"]
        log["food"] = row["food"]
    except:
        log = {}

    return log

def update_log(log):
    updated_log = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE logs SET username = ?, entry_time = ?, food = ? WHERE log_id =?",  
                     (log["username"], log["entry_time"], log["food"], log["log_id"],))
        conn.commit()
        #return the log
        updated_log = get_log_by_id(log["log_id"])

    except:
        conn.rollback()
        updated_log = {}
    finally:
        conn.close()

    return updated_log

def delete_log(log_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from logs WHERE log_id = ?",     
                      (log_id,))
        conn.commit()
        message["status"] = "log deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete log"
    finally:
        conn.close()
    return message

from flask_jwt_extended import jwt_required
@jwt_required()
@app.route('/api/logs', methods=['GET'])
def api_get_logs():
    return jsonify(get_logs())

@jwt_required()
@app.route('/api/logs/<log_id>', methods=['GET'])
def api_get_log(log_id):
    return jsonify(get_log_by_id(log_id))

@jwt_required()
@app.route('/api/logs/add',  methods = ['POST'])
def api_add_log():
    log = request.get_json()
    return jsonify(insert_log(log))

@jwt_required()
@app.route('/api/logs/update',  methods = ['PUT'])
def api_update_log():
    log = request.get_json()
    return jsonify(update_log(log))

@jwt_required()
@app.route('/api/logs/delete/<log_id>',  methods = ['DELETE'])
def api_delete_log(log_id):
    return jsonify(delete_log(log_id))