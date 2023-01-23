import json

def parsejsonexemple(): 
    with open('velo.txt') as f:
        data = json.load(f)
        
        name=data["features"][0]["properties"]["nom"]
        print(name)
        nom=[]
        for i in range(0, len(data["features"])): 
            nom.append(data["features"][i]["properties"]["nom"])
        print(nom)
        for i in range(len(nom)):
            print(nom[i])
        
        
        
        
        
        for i in range(len(nom)):
            f1=open(f"velo_{nom[i]}.txt","a",encoding="utf-8")
            f1.write(f"{nom[i]}"+ "\n" )
            f1.write(f"{data['features'][i]['properties']['installati']}" + "\n")
            f1.write(f"{data['features'][i]['properties']['commune']}" + "\n")
            f1.close()
            
            
            
"""
    tree = etree.parse(nom)
    for user in tree.xpath("Status"):
        print('Info Parking :',user.text)

    for name in tree.xpath("Name"):

        pass

    for total in tree.xpath("Total"):

        pass

    for user in tree.xpath("Free"): 

        pass

    for status in tree.xpath("Status"):

        pass



    f2.write(name.text+ status.text+ user.text+"\n")
    f2.close()
    return donnee.text




"""


tree = etree.parse(parkings)
for user in tree.xpath("Status"):
    f1=open(".txt","w",encoding='utf=8') 
    print('Info Parking :',user.text)

for name in tree.xpath("Name"):

    pass

for total in tree.xpath("Total"):

    pass

for user in tree.xpath("Free"): 
    pass
for status in tree.xpath("Status"):

    pass
