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
-- https://www.sqlitetutorial.net/sqlite-date-functions/sqlite-datetime-function/
    
CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY NOT NULL,
        password TEXT NOT NULL,
        height INTEGER NOT NULL
        weight INTEGER NOT NULL
        age INTEGER NOT NULL
    );

CREATE TABLE IF NOT EXISTS logs (
        log_id INTEGER NOT NULL PRIMARY KEY, 
        username TEXT, 
        entryTime DATETIME, 
        food TEXT
    );

CREATE TABLE IF NOT EXISTS progress (
        user_id INTEGER PRIMARY KEY NOT NULL,
        weight INTEGER NOT NULL,
        week INTEGER NOT NULL
    );


    