import requests


response = requests.get('https://httpbin.org/image/jpeg')
print(response.headers['content-type'])
with open('image_1.jpeg', 'wb') as img:
    img.write(response.content)

response = requests.get('https://httpbin.org/image/png')
print(response.headers['content-type'])
with open('image_1.png', 'wb') as img:
    img.write(response.content)

response = requests.get('https://httpbin.org/image/svg')
print(response.headers['content-type'])
with open('image_1.svg', 'wb') as img:
    img.write(response.content)

response = requests.get('https://httpbin.org/image/webp')
print(response.headers['content-type'])
with open('image_1.webp', 'wb') as img:
    img.write(response.content)

response = requests.get('https://httpbin.org/ip')
with open('my-ip.txt', 'w') as ip:
    ip.write(response.text)