import requests
from bs4 import BeautifulSoup

# C:\VTRoot\HarddiskVolume3\Users\testinium\Desktop\tez\

response = requests.get("https://www.trendyol.com/")

template = BeautifulSoup(response.content, 'html.parser')

banner = template.find_all('a', class_="widget widget-big-with-name", href=True)

file = open('kategoriler.txt', 'a')
for i in banner:
    file.write(i['href'] + "\n")
file.close()
print("dosya yazıldı")
