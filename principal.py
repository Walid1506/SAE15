from lxml import etree
import xml.etree.ElementTree as et

f1=open("FR_MTP_ANTI0.txt","r")


lignes=f1.readlines()
for ligne in lignes:
    ligne=ligne.replace('\n','')
    donnees=ligne.split("<?xml version='1.0' encoding='UTF-8'?> ")  
    
    tree=etree.parse("FR_MTP_ANTI0.txt","r")
    print(donnees)
    for us in tree.xpath("DateTime"):
        print(us.text)