import sqlite3

with sqlite3.connect('Chinook_Sqlite.sqlite') as con:
    cur = con.cursor()
    cur.execute('''SELECT * FROM Customer WHERE LENGTH(Company) == (SELECT MAX(LENGTH(Company)) FROM Customer)''')
    cur.execute('''SELECT COUNT(*) AS CustomerCount FROM Customer WHERE Company IS NULL AND Fax IS NULL''')
    cur.execute("""SELECT CASE
        WHEN Country IN ('USA', 'Canada', 'Mexico') THEN 'North America'
        WHEN Country IN ('France', 'Germany', 'Italy', 'Spain', 'United Kingdom', 
                         'Netherlands', 'Sweden', 'Norway', 'Switzerland', 'Poland') THEN 'Europe'
        WHEN Country IN ('Australia', 'New Zealand') THEN 'Australia'
        WHEN Country IN ('Brazil', 'Argentina', 'Chile', 'Colombia') THEN 'South America'
        WHEN Country IN ('China', 'India', 'Japan', 'South Korea') THEN 'Asia'
        WHEN Country IN ('South Africa', 'Egypt', 'Nigeria') THEN 'Africa'
        ELSE 'Unknown'
    END AS Continent, COUNT(*) AS CustomerCount FROM Customer GROUP BY Continent""")
    print(*cur.fetchall(), sep='\n')
