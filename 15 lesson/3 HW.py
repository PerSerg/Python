import requests
from bs4 import BeautifulSoup

response = requests.get("https://automarine.ru/eng/index.html") 
soup = BeautifulSoup(response.text, 'html.parser')
for i in soup.descendants:
    if i.name:
        print(i.name)
for tag in soup.find_all('h2'):
    print('H2', tag.text)
for tag in soup.find_all('h3'):
    print('H3', tag.text)
for tag in soup.find_all('span'):
    print('span', tag.text)