import os
from shutil import copy2,copyfile
import numpy as np

disease_dict = {"No Finding": "0",
                "Atelectasis": "",
                "Cardiomegaly": ""}

disease_classes = ['No Finding', 'Atelectasis', 'Cardiomegaly', 'Effusion',
                   'Infiltration', 'Mass', 'Nodule', 'Pneumonia', 'Pneumothorax', 'Consolidation',
                   'Edema', 'Emphysema', 'Fibrosis', 'Pleural_Thickening','Hernia']

root_dir = 'D:\Datasets\CXR\ChestXray14\images_all\\'
#my_folder = open('C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\\bin\Chest14\\new_data_entry.csv',"w")
main_data_entry = 'D:\Datasets\CXR\ChestXray14\Data_Entry_2017.csv'

linecount1 = 0
#### PATH BILGILERINI BILGISAYARA GORE AYARLAMA #####
"""
with open(main_data_entry, 'r') as f:
    header = f.readline()
    my_folder.write(header)

    for line in f:
        linecount1 +=1
        fields = line.strip('\n').split(',')
        fields[0] = root_dir + fields[0]
        yazilcakline = ''
        for h in range(len(fields)):
            yazilcakline = yazilcakline + fields[h] + ','

        my_folder.write(yazilcakline)
        my_folder.write("\n")
        
        a =1
"""
#my_folder.close()
linecount = 0
newpath = r'D:\Datasets\CXR\ChestXray14\Chest14_category'
my_folder1 = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\\bin\Chest14\\new_data_entry.csv'

counterb = np.zeros((15))

if not os.path.exists(newpath):
    os.makedirs(newpath)

with open(my_folder1, 'r') as f:
    header = f.readline()

    for k in disease_classes:
        newcategorypath = os.path.join(newpath,k)
        if not os.path.exists(newcategorypath):
            os.makedirs(newcategorypath)
    for line in f:
        linecount += 1
        fields = line.strip('\n').split(',')
        patient_diseases = fields[1].split('|')

        for disease in patient_diseases:
            j = disease_classes.index(disease)
            counterb[j] += 1
            copydest = os.path.join(newpath, disease)
            patientid = fields[0].split("\\")[-1]

            copyfiledest = os.path.join(copydest, patientid)
            copyfile(fields[0], copyfiledest)

        if linecount % 500 == 0:
            print('Devam...', linecount)

        a=1

print(disease_classes)
print(counterb)