import csv
ttt = []
with open(r"C:\Users\me\PycharmProjects\CheXpert\Chexpert\config\train.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile,delimiter = ' ', quotechar= '|')
    for row in spamreader:
        ttt.append(row)

myfer = open('C:\\Users\me\PycharmProjects\CheXpert\Chexpert\\eggs2.csv','w')
with myfer:
    writer = csv.writer(myfer)
    for row in ttt:
        writer.writerows(row)
'''
k = 0
for row in spamreader:
    k = k + 1
    if k > 2:
        a = row
        newa = a[0][35:]
        bolum1 = a[0][:41]
        gercek1 = "C:\\Users\me\PycharmProjects\CheXpert\Chexpert\CheXpert-v1.0-small\\"
        fon = gercek1 + newa

        spamwriter.writerow(fon)
        c = 1238
'''