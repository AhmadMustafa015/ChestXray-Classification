import csv
import numpy as np
import os
from shutil import copy2,copyfile
import random
from collections import defaultdict


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



x = open('C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\\valid_yeni.csv', "w")

with open(csv_path) as f:
    header = f.readline().strip('\n').split(',')
    for line in f:
        linecount += 1
        fields = line.strip('\n').split(',')

        for r,c in enumerate(disease_class_locs):
            if fields[c+5] == '1.0':
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
#a = sorted(list(dene1.keys()))

classlengths = []
for i in range(len(a)):
    for j in range(dene1[a[i]][0]):

        classid = int(dene1[a[i]][1][j] / numselect)
        index = dene1[a[i]][1][j] % numselect
        randselect[classid].remove(a[i])



validindex = []
validsetatilcak = 500
for p in range(len(disease_class_locs)):
    validindex.append([])
    validindex[p] = sorted(random.sample(randselect[p],validsetatilcak))






result = {x for l in randselect for x in l}
b = 1

print(header[5:])
















#temp = randselect[classid]
#cikcak = a[i]
#temp.remove(cikcak)


#allselect = sorted(allselect)
#uniqselect = list(set(allselect))
#list_difference = [item for item in uniqselect if item not in allselect]