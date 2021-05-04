#Adım 1
````
python kategoriler.py 
````
burası trendyola giderek kategori urllerini parse ederek alt-kategoriler.txt dosyasına yazar


#Adım 2
 ````
 python urun_toplama.py
````
burası kategoriler içindeki ürünlerin id değerlerini ayrıştırarak product-data-id.txt
dosyasına sırası ile ekler

#Adım 3
````
python yorum_yakalama.py
````
topalnan ürün idlerini
````
https://public-sdc.trendyol.com/discovery-web-productgw-service/api/review/{urun-id}
````
urline koyarak rest apiye GET isteği yollar ve gelen json datasını parse
ederek içindeki tüm yorumları alır ve tum_yorumlar.csv dosyasına ekler
