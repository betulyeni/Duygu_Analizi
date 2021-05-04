import requests
import csv

rest_api_url = "https://public-sdc.trendyol.com/discovery-web-productgw-service/api/review/{urun_id}?userId=12855011&merchantId=2471&storefrontId=1&culture=tr-TR&order=5&searchValue=&onlySellerReviews=false&page={page}"

yorumlari_alinan_urunler = []  # tekrar eden ürün idlerinin tekrar yorumlarının alınmasını önlemek için bir kontrol listesi
with open('product-data-id.txt', 'r') as file:
    for i in file.readlines():
        id = i.replace('\n', '')

        if not (id in yorumlari_alinan_urunler):  # eğer ürünün yorumları çekilmişse birkez daha çekmeyeceğiz
            yorum_url = rest_api_url.format(urun_id=id, page=1)
            yorum_data = requests.get(yorum_url).json()
            for i in range(1, yorum_data["result"]["productReviews"]["totalPages"] + 1):
                try:
                    yorum_url = rest_api_url.format(urun_id=id, page=i)

                    yorum_data = requests.get(yorum_url).json()

                    content = yorum_data["result"]["productReviews"]["content"]
                    print("product url :", yorum_url)
                    print("total pages :", yorum_data["result"]["productReviews"]["totalPages"])
                    if content: # eğer contet boş ise sayfa es geçilecek
                        with open('tum_yorumlar.csv', 'a', encoding="utf-8", newline='') as file:
                            fieldnames = ['yorumlar']
                            writer = csv.writer(file)
                            writer.writerow(fieldnames)
                            for i in content:
                                writer.writerow([i["comment"]])
                except:
                    # herhangi bir hata oluşursa orayı es geçip diğer ürüne atla
                    pass

        yorumlari_alinan_urunler.append(id)
