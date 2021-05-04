import requests
from bs4 import BeautifulSoup

file = open('kategoriler.txt', 'r')
lines = file.readlines()
file.close()

for i in lines:
    response = requests.get(i)
    template = BeautifulSoup(response.content, 'html.parser')
    banner = template.find_all('a', class_="campaign campaign-big", href=True)

    print(banner)
    alt_kategoriler = open('alt_kategoriler.txt', 'w')

    for i in banner:
        alt_kategoriler.write(i['href'] + "\n")
    alt_kategoriler.close()
