import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = 'https://www.trendyol.com'

kategoriler = open("products.txt", 'r')
lines = kategoriler.readlines()

for i in lines:
    response = requests.get(BASE_URL + i.replace('\n', '') + "/yorumlar")
    if response.status_code == 200:
        print(response.url, " yorumları alındı")
        template = BeautifulSoup(response.content, 'html.parser')

        command = template.find_all('div', class_="rnr-com-tx")
        with open('comments.csv', 'a', encoding="utf-8", newline='') as file:
            fieldnames = ['command']
            writer = csv.writer(file)
            writer.writerow(fieldnames)

            for i in command:
                writer.writerow([str(i.text)])
    else:
        print(i, " url ", response.status_code, " codu iel hata verdi")
