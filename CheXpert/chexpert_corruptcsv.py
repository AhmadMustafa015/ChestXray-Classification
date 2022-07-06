
corrupt_list = 'D:\Datasets\CXR\Chexpert\CheXpert-v1.0\\corrupt_patient_list.txt'

###### TXT DOSYASINA YAZILMIS BOZUK PATIENT ID LERDEN OLUSTURULAN LISTE
patientid_list = []
with open(corrupt_list, 'r') as f:
    for line in f:
        line = line[:-1]
        if line == '':
            break
        patientid_list.append(int(line))

uniqueids = list(set(patientid_list))

#### PATHLERIN BILGISAYARDAKI IMAGE YERLERINE GORE AYARLANMASI

train_csv_path = 'D:\Datasets\CXR\Chexpert\CheXpert-v1.0\\valid.csv'
new_train_csv = open('C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\Chexpert-Orig\\valid_orig_new_upd.csv', "w")
image_root_path = 'D:\Datasets\CXR\Chexpert\\'
linecount2 = 0
with open(train_csv_path, 'r') as f:
    header = f.readline()
    new_train_csv.write(header)
    new_train_csv.write("\n")

    for line in f:
        linecount2 +=1
        fields = line.strip('\n').split(',')
        fields[0] = image_root_path + fields[0]
        yazilcakline = ''
        for h in range(len(fields)):
            yazilcakline = yazilcakline + fields[h] + ','

        new_train_csv.write(yazilcakline)
        new_train_csv.write("\n")

        if (linecount2 % 100) == 0:
            print(linecount2)
'''

###### BOZUK PATIENTLARIN LISTEDEN CIAKRILMASI

orig_train_csv = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\Chexpert-Orig\\train_orig_new.csv'
upd_train_csv = open('C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\Chexpert-Orig\\train_orig_new_upd.csv', "w")

linecount1 = 0
imagediscarded = 0
with open(orig_train_csv, 'r') as f:
    header = f.readline()
    upd_train_csv.write(header)

    for line in f:
        linecount1 +=1
        fields = line.strip('\n').split(',')
        id = int(fields[0].split('/')[2][7:])
        if id not in uniqueids:
            upd_train_csv.write(line)
            #upd_train_csv.write("\n")
            imagediscarded += 1


        b = 1

print(imagediscarded)
'''

a =1
