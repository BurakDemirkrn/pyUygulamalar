import requests
from bs4 import BeautifulSoup
import time
while True:
    url = requests.get("https://www.getmidas.com/canli-borsa/xu100-bist-100-hisseleri")
    print(url.status_code)

    if url.status_code == 200:
        print("Siteden Veri Çekilebilir")
    else:
        print("Siteye ulaşılamıyor.")
        break

    soup = BeautifulSoup(url.content,"html.parser")
    veri = soup.find("tbody",{"class":"table-body"}).find_all("tr",{"class":"table-row"})

    for i in veri:
        sutunlar = i.find_all("td")
        print(sutunlar[0].text.strip(),sutunlar[1].text.strip())

    print("Yenilenmesine 10 sn")
    time.sleep(10)
