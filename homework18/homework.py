import sqlite3


def connect_database(database_name: str):
    with sqlite3.connect(database_name) as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE "Table1" (
            ContactId INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
            Username TEXT UNIQUE,
            CreditId INTEGER NOT NULL,
            IssueDate TEXT,
            Sum INTEGER
            )''')


connect_database('data_base.bd')
