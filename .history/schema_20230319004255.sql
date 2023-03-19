-- DROP TABLE IF EXISTS workouts;

-- CREATE TABLE workouts (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     username TEXT,
--     exercise TEXT, 
--     weight TEXT,
--     repititions TEXT,
--     time TEXT,
--     totalweight INTEGER,
--     created TEXT
    
-- );

-- foodpath
CREATE TABLE IF NOT EXISTS logs (
    entryID INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT, 
    entryTime DATETIME, 
    food TEXT, 
    servings INTEGER);
    
    CREATE TABLE IF NOT EXISTS users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    email TEXT,
    created DATETIME);