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
CREATE TABLE IF NOT EXISTS Journal (
    entryID INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT, 
    entryTime DATETIME, 
    food TEXT, 
    servings INTEGER);