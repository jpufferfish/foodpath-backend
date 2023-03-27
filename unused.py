# def get_logs():
#     logs = []
#     try:
#         conn = connect_to_db()
#         conn.row_factory = sqlite3.Row
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM logs")
#         rows = cur.fetchall()

#         # convert row objects to dictionary
#         for i in rows:
#             log = {}
#             log["log_id"] = i["log_id"]
#             log["username"] = i["username"]
#             log["entry_time"] = i["entry_time"]
#             log["food"] = i["food"]
#             logs.append(log)

#     except:
#         logs = []

#     return logs

# @jwt_required()
# @app.route('/logs/update',  methods = ['PUT'])
# def api_update_log():
#     log = request.get_json()
#     return jsonify(update_log(log))

# @jwt_required()
# @app.route('/logs/delete/<log_id>',  methods = ['DELETE'])
# def api_delete_log(log_id):
#     return jsonify(delete_log(log_id))

# history revision would be extra feature
# def update_log(log):
#     updated_log = {}
#     try:
#         conn = connect_to_db()
#         cur = conn.cursor()
#         cur.execute("UPDATE logs SET username = ?, entry_time = ?, food = ? WHERE log_id =?",  
#                      (log["username"], log["entry_time"], log["food"], log["log_id"],))
#         conn.commit()
#         #return the log
#         updated_log = get_log_by_id(log["log_id"])

#     except:
#         conn.rollback()
#         updated_log = {}
#         conn.close()

#     return updated_log

# extra feature
# def delete_log(log_id):
#     message = {}
#     try:
#         conn = connect_to_db()
#         conn.execute("DELETE from logs WHERE log_id = ?",     
#                       (log_id,))
#         conn.commit()
#         message["status"] = "log deleted successfully"
#     except:
#         conn.rollback()
#         message["status"] = "Cannot delete log"
#     finally:
#         conn.close()
#     return message