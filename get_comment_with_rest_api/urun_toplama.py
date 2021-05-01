import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.trendyol.com'

kategoriler = open("alt_kategoriler.txt", 'r')

lines = kategoriler.readlines()

for i in lines:
    response = requests.get(BASE_URL + i.replace('\n', ''))
    if response.status_code == 200:
        template = BeautifulSoup(response.content, 'html.parser')
        product_card = template.find_all('div', class_="boutique-product")

        print(product_card)
        with open("product-data-id.txt", 'a') as file:
            for i in product_card:
                file.write(str(i["data-id"]) + "\n")

    else:
        print(i, " url ", response.status_code, " codu iel hata verdi")
