import requests
import json
import sqlite3

todo_url = 'https://jsonplaceholder.typicode.com/todos'
user_url = 'https://jsonplaceholder.typicode.com/users'
todo_response = requests.get(f'{todo_url}')
user_response = requests.get(f'{user_url}')
connection = sqlite3.connect('todos and users.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS todos(userId INTEGER NOT NULL, id INTEGER PRIMARY KEY NOT NULL,' 
               'title TEXT NOT NULL, completed BOOLEAN NOT NULL)')
cursor.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL,'
               'username TEXT NOT NULL, email TEXT NOT NULL, address_street TEXT NOT NULL,'
               'address_suite TEXT NOT NULL, address_city TEXT NOT NULL, address_zipcode TEXT NOT NULL,'
               'address_geo_lat FLOAT NOT NULL, address_geo_lng FLOAT NOT NULL, phone TEXT NOT NULL,'
               'website TEXT NOT NULL, company_name TEXT NOT NULL, company_catchPhrase TEXT NOT NULL,'
               'company_bs TEXT NOT NULL)')
cursor.execute('delete from todos')
cursor.execute('delete from users')
for i in json.loads(todo_response.text):
    cursor.execute(f'INSERT INTO todos VALUES("{i["userId"]}", "{i["id"]}", "{i["title"]}",'
                   f'"{i["completed"]}")')


for i in json.loads(user_response.text):
    cursor.execute(f'INSERT INTO users VALUES("{i["id"]}", "{i["name"]}", "{i["username"]}",'
                   f'"{i["email"]}", "{i["address"]["street"]}", "{i["address"]["suite"]}",'
                   f'"{i["address"]["city"]}", "{i["address"]["zipcode"]}", "{i["address"]["geo"]["lat"]}",'
                   f'"{i["address"]["geo"]["lng"]}", "{i["phone"]}", "{i["website"]}",'
                   f'"{i["company"]["name"]}", "{i["company"]["catchPhrase"]}", "{i["company"]["bs"]}")')
connection.commit()
connection.close()