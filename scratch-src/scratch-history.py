# class mealtype(Enum):
#     BREAKFAST = 0
#     LUNCH = 1
#     DINNER = 2

# dont have to return the json of the usda api foods, just the food names
# because of just displaying history of logs
# when adding to this backend though, the specific food data will be added to csv
# def get_logs_by_username(username):
#     log = {}
#     try:
#         conn = connect_to_db()
#         conn.row_factory = sqlite3.Row
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM users WHERE username = ?", (username,))
#         row = cur.fetchone()
#         # convert row object to dictionary (but nested?)
#         log["timestamp"] = row["timestamp"]
#         log["username"] = row["username"]
#         log["entry_time"] = row["entry_time"]
#         log["food"] = row["food"]
#         todos = conn.execute('SELECT i.content, l.title FROM items i JOIN lists l \
#                         ON i.list_id = l.id ORDER BY l.title;').fetchall()
#         lists = {}
#         for k, g in groupby(todos, key=lambda t: t['title']):
#             lists[k] = list(g)
#     except:
#         log = {}

#     return log

# @app.route('/logs/<username>', methods=['GET'])
# @jwt_required()
# def api_get_logs(username):
#     return jsonify(get_logs_by_username(username))

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