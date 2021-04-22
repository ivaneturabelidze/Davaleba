import sqlite3

connection = sqlite3.connect('dataset2.db')
cursor = connection.cursor()
cursor.execute('create table if not exists sales(Order_Month integer not null, Order_Date integer not null,'
               'Order_Year integer not null, Region text not null, Client text not null, Item text not null,'
               'Units integer not null, UnitCost float not null, Total float not null)')

cursor.execute('delete from sales')

with open('dataset2.csv') as x:
    for i in x.readlines()[1:]:
        line = i.strip().split(',')
        for j in line:
            if j.startswith('"'):
                replaced = j.replace(j, j + line[line.index(j) + 1])
                line[line.index(j)] = replaced.strip('"')
                line.pop()
        date = line[0].split('/')
        cursor.execute(f'insert into sales values({int(date[0])}, {int(date[1])}, {int(date[2])}, "{line[1]}",'
                       f'"{line[2]}", "{line[3]}",{int(line[4])}, {float(line[5])}, {float(line[6])})')

cursor.execute('select * from sales')
eastSales = 0
centSales = 0
westSales = 0
customers = []
sales = []
highest = 0
customer = None
items = []
mostSoldUnits = 0
mostSoldItem = None
totalPrice = 0
avgPrice = 0
totalSold = 0

for i in cursor:
    if not customers.__contains__(i[4]):
        customers.append(i[4])
    if not items.__contains__(i[5]):
        items.append(i[5])
    sales.append(i)
    if i[3] == 'East':
        eastSales += i[8]
    elif i[3] == 'Central':
        centSales += i[8]
    elif i[3] == 'West':
        westSales += i[8]

for i in customers:
    total = 0
    for j in sales:
        if i == j[4]:
            total += j[8]
    if total > highest:
        highest = total
        customer = i
for i in items:
    totalSold = 0
    for j in sales:
        if i == j[5]:
            totalSold += j[6]
    if totalSold > mostSoldUnits:
        mostSoldUnits = totalSold
        mostSoldItem = i
for i in sales:
    totalPrice += i[7]
avgPrice = round(totalPrice / len(items), 2)
for i in sales:
    totalSold += i[8]
print('Total sales in Eastern region: ' + str(eastSales.__round__(2)))
print('Total sales in Central region: ' + str(centSales.__round__(2)))
print('Total sales in Western region: ' + str(westSales.__round__(2)))
print(customer)
print(mostSoldItem)
print(avgPrice)
print(round(totalSold, 2))
connection.commit()
connection.close()
