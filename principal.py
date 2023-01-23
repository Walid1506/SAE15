from lxml import etree
s1=open("FR_MTP_FOCH.txt","r")
tree=etree.parse("FR_MTP_FOCH.txt")
for user in tree.xpath("Name"):
    print(user.text)