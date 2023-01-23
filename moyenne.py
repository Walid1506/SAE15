import matplotlib.pyplot as plt
import xml
from lxml import etree
import pandas as pd

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_CAS_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']

data= pd.read_xml(parkings)
tree = etree.parse(parkings)
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

x = data.
y = data.

















































"""names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()"""