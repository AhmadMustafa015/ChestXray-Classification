import csv
import numpy as np
import os
from shutil import copy2,copyfile
import random

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










        for j in range(14):
            if fields[j + 5] == '1.0':
                counterb[j] += 1
                counterindb[j].append(linecount)
            if fields[j + 5] == '-1.0':
                counteruncert[j] += 1
                counterinduncert[j].append(linecount)


print(header[5:])
print(counterb)

print(counteruncert)
print(sum(counterb))
b =1