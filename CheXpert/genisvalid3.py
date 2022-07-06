import csv
import numpy as np
import os
from shutil import copy2,copyfile
import random
from collections import defaultdict

### DUPLICATE ( VALIDE ATILAN AYNI OLANLAR ) BULMA KODU
def getDuplicatesWithInfo(listOfElems):
    ''' Get duplicate element in a list along with thier indices in list
     and frequency count'''
    dictOfElems = dict()
    index = 0
    # Iterate over each element in list and keep track of index
    for elem in listOfElems:
        # If element exists in dict then keep its index in lisr & increment its frequency
        if elem in dictOfElems:
            dictOfElems[elem][0] += 1
            dictOfElems[elem][1].append(index)
        else:
            # Add a new entry in dictionary
            dictOfElems[elem] = [1, [index]]
        index += 1

    dictOfElems = {key: value for key, value in dictOfElems.items() if value[0] > 1}
    return dictOfElems


csv_path = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\\train.csv'
counterb = np.zeros((14))
counteruncert = np.zeros((14))
counterindb = []
counterinduncert = []
hastalikindex = []

for b in range(14):
    counterindb.append([])
    counterinduncert.append([])

linecount = 0
newpath = r'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\\Chexpert-newvalid'
if not os.path.exists(newpath):
    os.makedirs(newpath)

disease_classes = ['Cardiomegaly','Edema','Consolidation','Atelectasis', 'Pleural Effusion']
disease_class_locs = [2,5,6,8,10]

for c in range(len(disease_class_locs)):
    hastalikindex.append([])

## TANILAR ARASINDA -1 YOKSA INDEXLERINI KAYDEDIYORUZ ( SECTIGIMIZ 5 CLASS ICIN)
with open(csv_path) as f:
    header = f.readline().strip('\n').split(',')
    for line in f:
        linecount += 1
        fields = line.strip('\n').split(',')

        for r,c in enumerate(disease_class_locs):
            if fields[c+5] == '1.0':
                if '-1.0' not in fields[5:]:
                    hastalikindex[r].append(linecount)


numselect = 700
randselect = []
allselect = []
for u in range(len(disease_class_locs)):
    randselect.append([])
    randselect[u] = sorted(random.sample(hastalikindex[0],numselect))
    allselect = allselect + randselect[u]


dene1 = getDuplicatesWithInfo(allselect)
a = list(dene1.keys())
classlengths = []

### DUPLICATE OLANLARIN YERLERINI BULUP, ONLARI CIKARIYORUZ YENI VALID SETINDEN
for i in range(len(a)):
    for j in range(dene1[a[i]][0]):

        classid = int(dene1[a[i]][1][j] / numselect)
        index = dene1[a[i]][1][j] % numselect
        randselect[classid].remove(a[i])


## CIKARILANLARDAN SONRA KALANLARIN ARASINDAN TEKRARDAN 500 ER ORNEK CEKILIYOR
validindex = []
validsetatilcak = 500
tumvalidlines = []
for p in range(len(disease_class_locs)):
    validindex.append([])
    validindex[p] = sorted(random.sample(randselect[p],validsetatilcak))
    tumvalidlines = tumvalidlines + validindex[p]

tumvalidlines = sorted(tumvalidlines)
linecount2 = 0

### TRAIN.CSV DEN LINELAR YENI VALID_YENI .CSV YE AKTARILIYOR
x = open('C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\\valid_yeni.csv', "w")
with open(csv_path) as f:
    header = f.readline()
    x.write(header)
    for line in f:
        linecount2 += 1
        if linecount2 in tumvalidlines:
            x.write(line)

### Valid 1 ve 0 lari ayarlama, bosluklari doldurma
x = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\\valid_yeni.csv'
y = open('C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\\valid_yeni_upd.csv', "w")

linecount = 0
with open(x) as f:
    header = f.readline()
    y.write(header)
    for line in f:
        linecount += 1
        fields = line.strip('\n').split(',')
        yazilcakline = ''
        for h in range(5):
            yazilcakline = yazilcakline + fields[h] + ','

        for b in range(14):
            if fields[b+5] == '':
                fields[b+5] = '0.0'
            if b == 13:
                yazilcakline = yazilcakline + fields[b+5]
            else:
                yazilcakline = yazilcakline + fields[b + 5] + ','

        y.write(yazilcakline)
        y.write("\n")


yenivalid = open('C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\\valid_yeni_upd.csv', "a")
eskivalid = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\\valid.csv'

## eski ve yeni valid birlestirme
linecount = 0
with open(eskivalid) as f:
    header = f.readline()
    for line in f:
        yenivalid.write(line)

linecount2 = 0
eskitrain = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\\train_yeni.csv'
yenitrain = open('C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\\train_yeni_upd.csv', "w")
with open(eskitrain) as f:
    header = f.readline()
    for line in f:
        linecount2 += 1
        if linecount2 not in tumvalidlines:
            yenitrain.write(line)
b = 1
print(header[5:])












