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
    
-- CREATE TABLE IF NOT EXISTS users (
--         username TEXT PRIMARY KEY NOT NULL,
--         email TEXT PRIMARY KEY NOT NULL,
--         password TEXT NOT NULL,
--         height REAL NOT NULL
--         weight INTEGER NOT NULL
--         age INTEGER NOT NULL
--     );

        CREATE TABLE IF NOT EXISTS users (
        PRIMARY KEY (username, email),
            password TEXT NOT NULL,
            height REAL NOT NULL,
            weight INTEGER NOT NULL,
            age INTEGER NOT NULL
            );

CREATE TABLE IF NOT EXISTS logs (
        log_id INTEGER NOT NULL PRIMARY KEY, 
        username TEXT, 
        entryTime DATETIME, 
        food TEXT
    );ß

CREATE TABLE IF NOT EXISTS progress (
        user_id INTEGER PRIMARY KEY NOT NULL,
        weight INTEGER NOT NULL,
        week INTEGER NOT NULL
    );


    
-- INSERT INTO users (username, email, password, height, weight, age) VALUES (DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT)