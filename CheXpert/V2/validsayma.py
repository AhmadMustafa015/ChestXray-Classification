import csv
import numpy as np


#csv_path = 'C:/Users/RadioscientificOne/PycharmProjects/Aphrodite/CheXpert/Chexpert/CheXpert-v1.0-small/valid.csv'
csv_path = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\\valid.csv'
counterb = np.zeros((14))
mestium = 0
cardio = 0
with open(csv_path) as f:
    header = f.readline().strip('\n').split(',')
    for line in f:
        fields = line.strip('\n').split(',')
        for j in range(14):
            if fields[j+5] == '1.0':
                counterb[j] += 1
            ## caridomestium vs cardiomegaly hieararsi anlama

        if fields[2+5] == '1.0' and fields[1+5] == '0.0':
            cardio += 1
            print('parent dinlemiyorr')
        if fields[2+5] == '0.0' and fields[1+5] == '1.0':
            mestium += 1
            print('aferin cocuk')

        a = 1
print(header[5:])
print(counterb)
print(sum(counterb))