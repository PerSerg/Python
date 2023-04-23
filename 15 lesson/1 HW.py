import requests

response = requests.get("https://automarine.ru/eng/index.html")
print(response.text)