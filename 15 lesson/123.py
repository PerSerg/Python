# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://google.com")
# print(response.text)

# soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title)

# titles = soup.findAll("h1")   
# for title in titles:
#     print(title.text)

# ___________________________________ find or FINDALL________________________________

# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://google.com")
# print(response.text)

# soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title)
# titles = soup.select("h1", class="main-header")
# for title in titles:
#     print(title.text)

# _____________________________________ поиск по селектору_______________________________

# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://automarine.ru/eng/index.html") 
# # второй сайт угрожает безопасности
# soup = BeautifulSoup(response.text, 'html.parser')
# for i in soup.descendants:
#     if i.name:
#         print(i.name)

# ________________________________________ выудить теги ______________________________________

# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://automarine.ru/eng/index.html") 
# # второй сайт угрожает безопасности
# soup = BeautifulSoup(response.text, 'html.parser')
# for i in soup.descendants:
#     if i.name:
#         print(i.name)
# print(soup.h1.text)

# __________________________________ напечатать что-то конкретное ______________________________

# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://automarine.ru/eng/index.html") 
# # второй сайт угрожает безопасности
# soup = BeautifulSoup(response.text, 'html.parser')
# for i in soup.descendants:
#     if i.name:
#         print(i.name)
# print(soup.find('div', id='page'))

# __________________________________ поиск по ID ______________________________

# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://automarine.ru/eng/index.html") 
# # второй сайт угрожает безопасности
# soup = BeautifulSoup(response.text, 'html.parser')
# for i in soup.descendants:
#     if i.name:
#         print(i.name)
# for tag in soup.find_all('h2'):
#     print(tag.text)

    # ___________________________ поиск заголовков 2 ур ____________________________

import requests
from bs4 import BeautifulSoup

response = requests.get("https://automarine.ru/eng/index.html") 
# второй сайт угрожает безопасности
soup = BeautifulSoup(response.text, 'html.parser')
for i in soup.descendants:
    if i.name:
        print(i.name)
for tag in soup.find_all('h2'):
    print(tag.text)