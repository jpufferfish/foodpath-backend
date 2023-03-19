import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO workouts (username, exercise, weight, totalweight, repititions, time,created) VALUES (?,?,?,?,?,?,?)", ('Khal','back fly,back fly, back fly', '45,35,25','105','15,20,25', '12:34,12:44,12:54','2022-03-11'))

cur.execute("INSERT INTO workouts (username, exercise, weight, totalweight, repititions, time,created) VALUES (?,?,?,?,?,?,?)", ('Khal','squat, squat, squat', '200,235,225','660','15,20,25', '12:34,12:44,12:54','2022-03-12'))

connection.commit()
connection.close()