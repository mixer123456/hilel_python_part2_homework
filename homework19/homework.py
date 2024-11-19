import sqlite3
from pprint import pprint

with sqlite3.connect('Chinook_Sqlite.sqlite') as con:
    cursor  = con.cursor()
    print('TASK 1')
    cursor.execute('''SELECT * FROM Customer LIMIT 3''')
    pprint(cursor.fetchall(), width=500)
    print('-' * 50)

    print('TASK 2')
    cursor.execute('''SELECT SUM(Total) AS TotalSum FROM Invoice''')
    print(cursor.fetchall()[0][0])
    print('-' * 50)

    print('TASK 3')
    cursor.execute('''SELECT * FROM Invoice WHERE BillingCity = "Paris"''')
    pprint(cursor.fetchall(), width=100)
    print('-' * 50)

    print('TASK 4')
    cursor.execute('''SELECT InvoiceDate FROM Invoice ORDER BY InvoiceDate ASC LIMIT 1''')
    print(cursor.fetchall())
    print('-' * 50)

    print('TASK 5')
    cursor.execute('''SELECT InvoiceDate FROM Invoice ORDER BY InvoiceDate DESC LIMIT 1''')
    print(cursor.fetchall())
