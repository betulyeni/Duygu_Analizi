import requests
from bs4 import BeautifulSoup

kategoriler = open("kategoriler.txt", 'r')

lines = kategoriler.readlines()

for i in lines:
    response = requests.get(i.replace('\n', ''))
    if response.status_code == 200:
        template = BeautifulSoup(response.content, 'html.parser')

        product_card = template.find('div', class_="prdct-cntnr-wrppr")

        with open('products.txt', 'a') as file:
            for i in product_card.find_all('a', href=True):
                url = str(i["href"])
                url = url[:url.index('?')]
                file.write(url + "\n")

    else:
        print(i, " url ", response.status_code, " codu iel hata verdi")
