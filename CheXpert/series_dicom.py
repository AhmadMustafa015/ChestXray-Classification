import SimpleITK as sitk
import os
import pydicom
from pydicom import DataElement
#import matplotlib.pyplot as plt
from pydicom.data import get_testdata_files
import numpy as np
import random
from PIL import Image, ImageFont, ImageDraw



dic_path = 'C:\\Users\\RadioscientificOne\\PycharmProjects\Aphrodite\\vinbigdata-chest-xray-abnormalities-detection\\train\\0a0ac65c40a9ac441651e4bfbde03c4e.dicom'
dic_path2 = 'D:\\Datasets\\manifest-1600709154662\\LIDC-IDRI\LIDC-IDRI-0001\\1.3.6.1.4.1.14519.5.2.1.6279.6001.298806137288633453246975630178\\1.3.6.1.4.1.14519.5.2.1.6279.6001.179049373636438705059720603192\\1-002.dcm'
dic_path3= 'D:\\Datasets\manifest-1600709154662\LIDC-IDRI\LIDC-IDRI-0001\\1.3.6.1.4.1.14519.5.2.1.6279.6001.175012972118199124641098335511\\1.3.6.1.4.1.14519.5.2.1.6279.6001.141365756818074696859567662357\\1-1.dcm'
ds = pydicom.filereader.dcmread(dic_path)
rowinfo = ds.Rows
ds.add_new('0x200011','IS',778899)
series = int(ds[0x20,0x11].value)
rowinfo2 = ds[0x28,0x10].value
#series = ds.
#ds.add_new('0x181050', 'DS', ['1.000000', '1.000000', '1.000000'])
print(ds)


series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(dic_path)
#print(series_IDs)

ds = pydicom.filereader.dcmread(dic_path2)
print(ds)

def append_output3(dicomfile, disease_classes, results,desti):  #dicomfile is a path, disease_classes, results are lists

    ds = pydicom.dcmread(dicomfile)   #reading dcm
    rows, columns = ds.pixel_array.shape    #would-be shape of caption canvas
    # dicom_pixel_dtype = ds.pixel_array.dtype
    img = Image.new(mode="I;16", size=(columns, rows))  #Notice that this is columns, rows  not rows, columns
    draw = ImageDraw.Draw(img)

    # use a truetype font
    font = ImageFont.truetype("arial.ttf", size=160)
    #caption stuff
    d_size = len(disease_classes)
    text = f""""""
    for i in range(d_size):
        text += f" {disease_classes[i]}  .........  {results[i]} \n"

    draw.multiline_text((10, 25), text, font=font)

    px = list(img.getdata())
    captionpixels = np.array(px, dtype=np.uint16).reshape((rows, columns))   #dtype conversion
    dicompixels=ds.pixel_array
    bigpixar = np.hstack((dicompixels, captionpixels))      #putting two together
    ds.Rows, ds.Columns = bigpixar.shape
    packed_pixel = bigpixar.tobytes()
    ds.PixelData = packed_pixel                             #packing it back into dcm
    newseriesnumber = random.randint(0,100000)
    ds.add_new('0x200011', 'IS', newseriesnumber)                     # IMAGE SERIES NUMBER ADDITION
    #filedir, file, blank = dicomfile.rpartition(".dicom") ### uzantiya adaptif bir yapi uretme
    #ds.save_as(filedir + "Radiologics" + file)              #Radiologics signature
    ds.save_as(modif_path)

###### original dicomlari jpeg isminden cekme ### 25.05
###### dicomlari ve islenmis dicomlari bir dosyada toplama
root_dicom_path = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\\vinbigdata-chest-xray-abnormalities-detection\\train\\'
out_csv_path = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\\bin\\test\\test_pacs_demo.csv'
dst = 'D:\\Datasets\\PACS_DEMO_DICOM'

from shutil import copyfile
import shutil


with open(out_csv_path) as f:
    header = f.readline()
    fields = header.strip('\n').split(',')
    classes = []
    for j in fields:
        classes.append(j)
    classes = classes[1:]
    for line in f:
        fields = line.strip('\n').split(',')
        base_name = os.path.basename(fields[0])
        dicom_name = os.path.splitext(base_name)[0]
        dicom_full_path = root_dicom_path + dicom_name + '.dicom'
        src = dicom_full_path
        modif_path = root_dicom_path + dicom_name + 'Radiologics' + '.dicom'
        results = []
        for count, j in enumerate(fields):
            if count > 0:
                g = round(float(j),4)
                results.append(g)

        #copyfile(src, dst)
        ##### KODDA DEGISEN KISIMLAR VAR, SON HALI JPEG2DICOM ICERISINDEKI SERIES_DICOMDA DURUO
        shutil.copy(src,dst)
        append_output3(src,classes,results,modif_path)



        b = 1



a =1