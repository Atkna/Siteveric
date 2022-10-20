from asyncore import write
from lib2to3.pytree import convert
import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook,load_workbook
import csv
import numpy as np
import xlsxwriter
import xlrd

eksen = open("C:\\Users\\3drea\\Desktop\\Siteveric-main\\3eksen.txt")

eksenoku = eksen.read()

url = eksenoku

dream = open("C:\\Users\\3drea\\Desktop\\Siteveric-main\\3dream.txt")

dreamoku = dream.read()

url2 = dreamoku

robo = open("C:\\Users\\3drea\\Desktop\\Siteveric-main\\robo.txt")

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

reskifiyat = soup.find_all("class",{"ins":"price dib mb__5"})
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
    robofiyat[i] = (robofiyat[i].text).strip("\n").replace("\n","").strip("KDV Dahil").replace("KDV Dahil ","")
    try:
     roboeskifiyat[i] = (roboeskifiyat[i].text).strip("").replace("KDV Dahil"," ").strip() 
     robomEskiFiyat = roboeskifiyat[i].strip("\n").replace("","")
    except IndexError:
        robomEskiFiyat = ""
    roboliste.append([roboisim[i],robofiyat[i],robomEskiFiyat])

df = pd.DataFrame(liste,columns = ["İsmi","Fiyat","Eski Fiyat"])
dfr = pd.DataFrame(rliste,columns = ["İsmi","Fiyat","sEski Fiyat"])
dfrobo = pd.DataFrame(roboliste,columns = ["İsmi","Fiyat","roboEski Fiyat"])

#excel dosyası yazdırma
#wb = Workbook()
#ws = wb.active

#df.save("liste.xlsx")
#wb = Workbook()

#sayfa = wb.active

#planWorkbook = xlsxwriter.Workbook("C:\\Users\\3drea\\Desktop\\Siteveric-main\\deneme.xlsx")
#planSheet = planWorkbook.add_worksheet("fiyatlar")

#inputWorkbook = xlrd.open_workbook(df)

#df.to_excel("C:\\Users\\3drea\\Desktop\\Siteveric-main\\deneme1.xlsx", engine='xlsxwriter',sheet_name='3EKSEN'  )
dfr.to_excel("C:\\Users\\3drea\\Desktop\\Siteveric-main\\deneme1.xlsx", engine='xlsxwriter',sheet_name='3dream'  )   
#harfler = ["A","B","C","D"]
#notlar = [85, 70, 55, 45]

#planSheet.write("B1","Notlar")

#planSheet.write(1,0, harfler[0])
#planSheet.write("A3", harfler[1])
#planSheet.write("A4", harfler[2])
#planSheet.write("A5", harfler[3])

#planSheet.write("B2", harfler[0])
#planSheet.write("B3", harfler[1])
#planSheet.write("B4", harfler[2])
#planSheet.write("B5", harfler[3])


#sayfa.title = "İlk Çalışma Alanı"

#sayfa = wb.create_sheet("Posta Kodları")
#sayfa = wb.create_sheet("Ülkeler")

#ws.append(["deneme","1","2"])
#print(wb.sheetnames) 

#wb.save("C:\\Users\\3drea\\Desktop\\Siteveric-main\\dosyaAdi.xlsx")

print(dfr)
print(df)
print(dfrobo)
