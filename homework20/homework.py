import sqlite3

with sqlite3.connect('Chinook_Sqlite.sqlite') as con:
    cur = con.cursor()
    cur.execute('''SELECT * FROM Customer WHERE LENGTH(Company) == (SELECT MAX(LENGTH(Company)) FROM Customer)''')
    cur.execute('''SELECT COUNT(*) AS CustomerCount FROM Customer WHERE Company IS NULL AND Fax IS NULL''')
    cur.execute("""SELECT CASE
            WHEN Country IN ('USA', 'Canada', 'Mexico') THEN 'North America'
            WHEN Country IN ('France', 'Germany', 'Italy', 'Spain', 'United Kingdom', 'Portugal', 
                             'Netherlands', 'Belgium', 'Sweden', 'Norway', 'Denmark', 'Finland',
                             'Ireland', 'Switzerland', 'Austria', 'Poland', 'Czech Republic', 'Hungary') THEN 'Europe'
            WHEN Country IN ('Australia', 'New Zealand', 'Fiji', 'Papua New Guinea') THEN 'Australia'
            WHEN Country IN ('Brazil', 'Argentina', 'Chile', 'Colombia', 'Peru', 'Venezuela', 'Uruguay', 'Paraguay') THEN 'South America'
            WHEN Country IN ('China', 'India', 'Japan', 'South Korea', 'Indonesia', 'Malaysia', 'Thailand', 'Vietnam', 'Philippines', 
                             'Pakistan', 'Bangladesh', 'Sri Lanka', 'Nepal', 'Myanmar', 'Singapore') THEN 'Asia'
            WHEN Country IN ('South Africa', 'Egypt', 'Nigeria', 'Kenya', 'Morocco', 'Ghana', 'Algeria', 'Ethiopia', 'Tanzania', 'Uganda') THEN 'Africa'
        END AS Continent, COUNT(*) AS CustomerCount FROM Customer WHERE Country IS NOT NULL GROUP BY Continent""")
    print(*cur.fetchall(), sep='\n')
