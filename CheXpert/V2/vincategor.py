import csv
import numpy as np
import os
from shutil import copy2,copyfile

csv_path = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\VinBigJPG\\train_down_new1.csv'
counterb = np.zeros((15))
linecount = 0
newpath = r'D:\Datasets\Totalkategori-vin'
if not os.path.exists(newpath):
    os.makedirs(newpath)


with open(csv_path) as f:
    header = f.readline().strip('\n').split(',')
    for k in range(15):
        newcategorypath = os.path.join(newpath,header[k+5])
        if not os.path.exists(newcategorypath):
            os.makedirs(newcategorypath)

    for line in f:
        linecount +=1
        fields = line.strip('\n').split(',')
        for j in range(15):
            if fields[j+5] == '1.0':
                counterb[j] += 1
                copydest = os.path.join(newpath,header[j+5])
                patientid =  fields[0].split("\\")[-1]

                copyfiledest = os.path.join(copydest,patientid)
                #copyfiledest = copyfiledest + '.jpg'
                copyfile(fields[0],copyfiledest)
                #copy2(fields[0],copydest)



        a = 1
print(header[5:])
print(counterb)
print(sum(counterb))