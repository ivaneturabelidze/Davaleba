import requests
import json

url = 'https://crudcrud.com/api/0923eb0ed8f54296886f4aee15670f4a'
header = {'content-type':'application/json'}
employee = {'id':1, 'name':'Nichola', 'surname':'Davies', 'age':34, 'gender':'Male', 'salary':1230}
response = requests.post(f'{url}/employees', data=json.dumps(employee), headers=header)
employee = {'id':2, 'name':'Deirdre', 'surname':'Paterson', 'age':41, 'gender':'Female', 'salary':1000}
response = requests.post(f'{url}/employees', data=json.dumps(employee), headers=header)
employee = {'id':3, 'name':'Sonia', 'surname':'Butler', 'age':28, 'gender':'Female', 'salary':1500}
response = requests.post(f'{url}/employees', data=json.dumps(employee), headers=header)
employee = {'id':4, 'name':'Jacob', 'surname':'Metcalfe', 'age':42, 'gender':'Male', 'salary':2000}
response = requests.post(f'{url}/employees', data=json.dumps(employee), headers=header)
employee = {'id':5, 'name':'Fiona', 'surname':'Clarkson', 'age':39, 'gender':'Female', 'salary':1850}
response = requests.post(f'{url}/employees', data=json.dumps(employee), headers=header)
response = requests.get(f'{url}/employees')
emp_list = json.loads(response.text)
for i in emp_list:
    if(i['id'] == 3):
        i['salary'] = 1700
        id = i['_id']
        del i['_id']
        requests.put(f'{url}/employees/{id}', data=json.dumps(i), headers=header)
    elif(i['id'] == 1):
        i['name'] = 'Nicholas'
        id = i['_id']
        del i['_id']
        requests.put(f'{url}/employees/{id}', data=json.dumps(i), headers=header)
    elif(i['id'] == 5):
        i['age'] = 40
        id = i['_id']
        del i['_id']
        requests.put(f'{url}/employees/{id}', data=json.dumps(i), headers=header)
    elif(i['id'] == 4):
        requests.delete(f'{url}/employees/{i["_id"]}')
response = requests.get(f'{url}/employees')
print(response.text)
