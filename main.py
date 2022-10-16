from lib2to3.pytree import convert
import requests
from bs4 import BeautifulSoup
import pandas as pd

eksen = open("C:\\Users\\ataka\\Desktop\\Sitev\\3eksen.txt")

eksenoku = eksen.read()

url = eksenoku

dream = open("C:\\Users\\ataka\\Desktop\\Sitev\\3dream.txt")

dreamoku = dream.read()

url2 = dreamoku

robo = open("C:\\Users\\ataka\\Desktop\\Sitev\\robo.txt")

robooku = robo.read()

url3 = robooku

#3eksen
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

eskifiyat = soup.find_all("div",{"class":"showcase-price-old"})
fiyat = soup.find_all("div",{"class":"showcase-price-new"})
isim = soup.find_all("div",{"class":"showcase-title"})

liste = list()

for i in range(len(isim)):
 
    mEskiFiyat = ""
    isim[i] = (isim[i].text).strip("\n").strip("\t")
    fiyat[i] = (fiyat[i].text).strip("\n").replace("\nTL"," TL").strip()
    try:
     eskifiyat[i] = (eskifiyat[i].text).strip("\n").replace("\nTL"," TL").strip() 
     mEskiFiyat = eskifiyat[i]
    except IndexError:
        mEskiFiyat = ""
    liste.append([isim[i],fiyat[i],mEskiFiyat])


#3dream
response = requests.get(url2)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

reskifiyat = soup.find_all("div",{"class":"showcase-price-old"})
rfiyat = soup.find_all("span",{"class":"price dib mb__5"})
risim = soup.find_all("a",{"class":"cd chp"})

rliste = list()

for i in range(len(risim)):
 
    rmEskiFiyat = ""
    risim[i] = (risim[i].text).strip("\n").strip("\n")
    rfiyat[i] = (rfiyat[i].text).strip("\n").replace("TL"," TL").strip("\n")
    try:
     reskifiyat[i] = (reskifiyat[i].text).strip("").replace("TL"," TL").strip() 
     rmEskiFiyat = reskifiyat[i]
    except IndexError:
        rmEskiFiyat = ""
    rliste.append([risim[i],rfiyat[i],rmEskiFiyat])
    
    #roboboloq
response = requests.get(url3)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

roboeskifiyat = soup.find_all("div",{"class":"showcase-price-old"})
robofiyat = soup.find_all("div",{"class":"discountPrice"})
roboisim = soup.find_all("div",{"class":"productName detailUrl"})

roboliste = list()

for i in range(len(roboisim)):
 
    robomEskiFiyat = ""
    roboisim[i] = (roboisim[i].text).strip("\n").strip("\n")
    robofiyat[i] = (robofiyat[i].text).strip("\n").replace("\n","").replace("KDV Dahil","")
    try:
     roboeskifiyat[i] = (roboeskifiyat[i].text).strip("").replace(""," ").strip() 
     robomEskiFiyat = roboeskifiyat[i].strip("\n").replace("","")
    except IndexError:
        robomEskiFiyat = ""
    roboliste.append([roboisim[i],robofiyat[i],robomEskiFiyat])

df = pd.DataFrame(liste,columns = ["İsmi","Fiyat","Eski Fiyat"])
dfr = pd.DataFrame(rliste,columns = ["İsmi","Fiyat","sEski Fiyat"])
dfrobo = pd.DataFrame(roboliste,columns = ["İsmi","Fiyat","roboEski Fiyat"])

print(dfr)
print(df)
print(dfrobo)