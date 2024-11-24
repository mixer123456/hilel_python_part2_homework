import sqlite3

with sqlite3.connect('Chinook_Sqlite.sqlite') as con:
    cur = con.cursor()
    cur.execute('''SELECT * FROM Customer WHERE LENGTH(Company) == (SELECT MAX(LENGTH(Company)) FROM Customer)''')
    cur.execute('''SELECT COUNT(*) AS CustomerCount FROM Customer WHERE Company IS NULL AND Fax IS NULL''')
    cur.execute("""SELECT CASE
        WHEN Phone LIKE '+1%' THEN 'North America'
        WHEN Phone LIKE '+2%' THEN 'Africa'
        WHEN Phone LIKE '+3%' OR Phone LIKE '+4%' THEN 'Europe'
        WHEN Phone LIKE '+5%' THEN 'South America'
        WHEN Phone LIKE '+6%' THEN 'Australia'
        WHEN Phone LIKE '+8%' OR Phone LIKE '+9%' THEN 'Asia'
        ELSE 'Unknown'
    END AS Continent, COUNT(*) AS CustomerCount FROM Customer GROUP BY Continent;""")
    print(*cur.fetchall(), sep='\n')
