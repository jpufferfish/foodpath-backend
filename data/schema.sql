-- quick copy-paste into smthn like mysql workbench for testing

CREATE TABLE IF NOT EXISTS history (
    timestamp TIMESTAMP PRIMARY KEY NOT NULL UNIQUE DEFAULT CURRENT_TIMESTAMP, 
    food TEXT NOT NULL,
    mealtype TEXT CHECK( pType IN ('BREAKFAST', 'LUNCH', 'DINNER' )),
    FOREIGN KEY (username) REFERENCES users(username)
    );