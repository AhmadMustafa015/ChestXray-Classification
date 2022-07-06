import csv

#dosya = "C:\Users\me\PycharmProjects\CheXpert\Chexpert\config\train.csv"
#C:\Users\me\PycharmProjects\CheXpert\Chexpert\CheXpert-v1.0-small\train\patient00001\study1\view1_frontal.jpg,Female,68,Frontal,AP,1.0,,,,,,,,,0.0,,,,1.0
#/nas/public/CheXpert/CheXpert-v1.0/train/patient00002/study2/view1_frontal.jpg,Female,87,Frontal,AP,,,-1.0,1.0,,-1.0,-1.0,,-1.0,,-1.0,,1.0,

'''
import pandas as pd

# making data frame from the csv file
dataframe = pd.read_csv("C:\\Users\me\PycharmProjects\CheXpert\Chexpert\config\\train.csv")

# using the replace() method
dataframe.replace(to_replace='/nas/public/CheXpert/CheXpert-v1.0/',
                  value="C:\\Users\me\PycharmProjects\CheXpert\Chexpert\CheXpert-v1.0-small\\",
                  inplace=True)

# writing  the dataframe to another csv file
dataframe.to_csv('C:\\Users\me\PycharmProjects\CheXpert\Chexpert\\outputfile.csv',
                 index=False)
'''

text = open("C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\\train.csv", "r")

# join() method combines all contents of
# csvfile.csv and formed as a string
text = ''.join([i for i in text])

# search and replace the contents
text = text.replace('C:\\Users\me\PycharmProjects\CheXpert\Chexpert\CheXpert-v1.0-small\\', "C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\\")

#C:\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\valid\patient64541

# output.csv is the output file opened in write mode
x = open('C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\CheXpert-v1.0-small\\train.csv', "w")

# all the replaced text is written in the output.csv file
x.writelines(text)
x.close()