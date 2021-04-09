import sqlite3
connection = sqlite3.connect('census.db')
cursor = connection.cursor()
cursor.execute('select * from density')
for i in cursor:
    print(i)
cursor.execute('select population from density')
for i in cursor:
    print(i)
cursor.execute('select * from density where population < 1000000')
for i in cursor:
    print(i)
cursor.execute('select * from density where population < 1000000 or population > 5000000')
for i in cursor:
    print(i)
cursor.execute('select * from density where population > 1000000 and population < 5000000')
for i in cursor:
    print(i)
cursor.execute('select population from density where land_area > 200000')
for i in cursor:
    print(i)
cursor.execute('select population/land_area from density')
for i in cursor:
    print(i)
connection.commit()