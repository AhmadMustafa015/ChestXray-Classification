import numpy as np
import os
from shutil import copy2,copyfile
import random
import pandas as pd

disease_dict = {"No finding": "14",
                "Aortic enlargement": "0",
                "Atelactasis": "1",
                "Calcification": "2",
                "Cardiomegaly": "3",
                "Consolidation": "4",
                "ILD": "5",
                "Infiltration": "6",
                "Lung Opacity": "7",
                "Nodule/Mass": "8",
                "Other Lesion": "9",
                "Pleural Effusion": "10",
                "Pleural Thickening": "11",
                "Pneumothorax": "12",
                "Pulmonary fibrosis": "13"}

orgcsv = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\VinBigJPG\\train_downsampled.csv'
newcsv = open('C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\VinBigJPG\\train_down_new1.csv', "w")
linecount = 0




with open(orgcsv) as f:
    header = f.readline().strip('\n').split(',')
    header_new = 'Path,Sex,Age,Frontal/Lateral,AP/PA,Aortic enlargement,Atelactasis,Calcification,Cardiomegaly,' \
                 'Consolidation,ILD,Infiltration,Lung Opacity,Nodule/Mass,Other Lesion,Pleural Effusion,Pleural Thickening,' \
                 'Pneumothorax,Pulmonary fibrosis,No Finding'
    newcsv.write(header_new)
    newcsv.write("\n")
    for line in f:

        linecount += 1
        newline = ""
        root_loc = "C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\VinBigJPG\\train\\train\\"
        fields = line.strip('\n').split(',')
        disease = fields[2]
        disease_categ = ''
        for j in range(15):
            if j == int(disease):
                disease_categ = disease_categ + '1.0,'
            else:
                disease_categ = disease_categ + '0.0,'

        ## NEW CSV LINE COMPONENTS
        image_path = root_loc + fields[0] + '.jpg,'
        inbetween = 'Sex,Age,Frontal,PA,'
        newline = newline+ image_path + inbetween + disease_categ
        newcsv.write(newline)
        newcsv.write("\n")
        a =1
