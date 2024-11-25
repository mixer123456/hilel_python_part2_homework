import sqlite3


def create_database(database_name: str):
    with open(f'{database_name}.sqlite', mode='w'):
        print('database created')

# create_database('database')

def connect_and_edit_database(database_name: str):
    with sqlite3.connect(f'{database_name}.sqlite') as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS  "Table1" (
            ContactId INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
            Username TEXT UNIQUE,
            CreditId INTEGER NOT NULL,
            IssueDate TEXT,
            Total INTEGER
            )''')

connect_and_edit_database('database')




