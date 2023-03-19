DROP TABLE IF EXISTS workouts;

CREATE TABLE workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    exercise TEXT, 
    weight TEXT,
    repititions TEXT,
    time TEXT,
    totalweight INTEGER,
    created TEXT
    
);