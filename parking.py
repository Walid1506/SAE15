import requests
from lxml import etree
import shutil
import time


parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_CAS_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']


def parking(parkings):
    lien = "https://data.montpellier3m.fr/sites/default/files/ressources/"+parkings+".xml"

    donnee=requests.get(lien)
   
    return donnee.text


heure=0
x=0
while x!=2:
    for i in parkings:
        nom=i
        print(parking(i))
        f1=open(nom+str(x)+".txt","a", encoding='utf8')
        f1.write(parking(i))
       
    
    time.sleep(3600)


    

