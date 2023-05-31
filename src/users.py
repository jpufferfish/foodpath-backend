# https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb
#!/usr/bin/python
import sqlite3, csv
from flask import Flask, request, jsonify #added to top of file
from flask_cors import CORS #added to top of file
from __main__ import app
CORS(app, resources={r"/*": {"origins": "*"}})

# https://charlesleifer.com/blog/going-fast-with-sqlite-and-python/
def connect_to_db():
    conn = sqlite3.connect('../data/database.db', timeout=10, isolation_level=None)
    conn.execute('pragma journal_mode=wal')
    return conn

def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''
CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            height REAL NOT NULL,
            weight INTEGER NOT NULL,
            age INTEGER NOT NULL
            );
        ''')
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

# inserting json
def insert_user(user):
    create_db_table()
    inserted_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, email, password, height, weight, age) VALUES (?, ?, ?, ?, ?, ?)"
                    , (user['username'], user['email'], user['password'], int(user['height'])/100, int(user['weight']), int(user['age'])) )
        conn.commit()
        inserted_user = user
    except Exception as e:
        print(e)
        conn().rollback()
    finally:
        conn.close()
    return inserted_user

# def get_users():
#     users = []
#     try:
#         conn = connect_to_db()
#         conn.row_factory = sqlite3.Row
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM users")
#         rows = cur.fetchall()
#         # convert row objects to dictionary
#         for i in rows:
#             user = {}
#             user["username"] = i["username"]
#             user["email"] = i["email"]
#             user["password"] = i["password"]
#             user["height"] = i["height"]
#             user["weight"] = i["weight"]
#             user["age"] = i["age"]
#             users.append(user)
#     except:
#         print('EMPTY USERS')
#         users = []
#     return users

def get_user_by_username(username):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", 
                       (username,))
        row = cur.fetchone()
        # convert row object to dictionary
        user["username"] = row["username"]
        user['email'] = row['email']
        user["password"] = row["password"]
        user["height"] = row["height"]
        user["weight"] = row["weight"]
        user["age"] = row["age"]
    except Exception as e:
        print(e)
        user = {}
    return user

# def update_user(user):
#     updated_user = {}
#     try:
#         conn = connect_to_db()
#         cur = conn.cursor()
#         cur.execute("UPDATE users SET email = ?, password = ?, height = ?, weight = ?, age = ? WHERE username =?",  
#                      (user['email'], user["password"], user["height"], user["weight"], user["age"], user["username"],))
#         conn.commit()
#         # idk if this function's connection still going
#         updated_user = get_user_by_username(user["username"])
#     except:
#         conn.rollback()
#         updated_user = {}
#     finally:
#         conn.close()
#     return updated_user

# username is same as username
# def delete_user(username):
#     message = {}
#     try:
#         conn = connect_to_db()
#         conn.execute("DELETE from users WHERE username = ?",     
#                       (username,))
#         conn.commit()
#         message["status"] = "User deleted successfully"
#     except:
#         conn.rollback()
#         message["status"] = "Cannot delete user"
#     finally:
#         conn.close()
#     return message

from flask_jwt_extended import jwt_required

# @app.route('/users', methods=['GET'])
# @jwt_required()
# # realisitically this prob wouldnt be used
# def api_get_users():
#     return jsonify(get_users())

@app.route('/users/<username>', methods=['GET'])
# @jwt_required()
def api_get_user(username):
    return jsonify(get_user_by_username(username))

# doesnt need jwt
@app.route('/users/add',  methods = ['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(insert_user(user))

# @app.route('/users/update',  methods = ['PUT'])
# @jwt_required()
# def api_update_user():
#     user = request.get_json()
#     return jsonify(update_user(user))

# @app.route('/users/delete/<username>',  methods = ['DELETE'])
# @jwt_required()
# def api_delete_user(username):
#     return jsonify(delete_user(username))