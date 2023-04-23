import requests
from bs4 import BeautifulSoup

response = requests.get("https://automarine.ru/eng/index.html") 
# второй сайт угрожает безопасности
soup = BeautifulSoup(response.text, 'html.parser')
for i in soup.descendants:
    if i.name:
        print(i.name)
print('Начало', soup.find('div', id='about_us'), 'Конец')

