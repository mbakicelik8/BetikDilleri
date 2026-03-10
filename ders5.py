import requests
from bs4 import BeautifulSoup
url='https://www.milligazete.com.tr/arsiv' #Mehmet Baki Çelik
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
list2= soup.find_all("div",{"class":"col-lg-6"})
for i in list2:
    for link in i.find_all('a'):
        my_link=link.get('href')+"\n"

        bas='https://www.milligazete.com.tr'
        yeni_link='{}{}'.format(bas,my_link)
        print(yeni_link)
        with open("baki2.txt","a",encoding="utf-8")as file:
            file.write(yeni_link.strip()+"\n")

import requests
from bs4 import BeautifulSoup
urr=('https://www.milligazete.com.tr/iran-ordusu-israil-ve-abd-buyukelcilerini-sinir-disi-eden-arap-veya-avrupa-ulkeleri-hurmuz-bogazindan-gecebilir')
r=requests.get(urr)
soup=BeautifulSoup(r.content,'html.parser')
date=(soup.find("div",{"class":"article-text container-padding"}).find_all('p'))
title=soup.find("p").getText()
print(title)






