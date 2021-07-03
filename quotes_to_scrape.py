import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
main_soup = BeautifulSoup(response.text, 'lxml')
tag_text = True
authors = []

while tag_text:
    for i in main_soup.find_all('a'):
        tag_text = None
        if 'Next' in i.text:
            next_page_url = url + i.attrs.get('href')
            response = requests.get(next_page_url)
            main_soup = BeautifulSoup(response.text, 'lxml')
            #print(next_page_url)
            tag_text = i.text
            break
        if i.text == "(about)":
            new_url = url + i.attrs.get('href')
            response = requests.get(new_url)
            auth_soup = BeautifulSoup(response.text, 'lxml')
            author = auth_soup.find('h3', {'class':'author-title'}).text.strip()
            if not author in authors:
                print(author)
                print(auth_soup.find('span', {'class':'author-born-date'}).text.strip())
                print(auth_soup.find('div', {'class':'author-description'}).text.strip())
                authors.append(author)