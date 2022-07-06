import numpy as np
import os
import pydicom
from pydicom import DataElement
import matplotlib.pyplot as plt
from pydicom.data import get_testdata_files
import numpy as np

from PIL import Image, ImageFont, ImageDraw


mainfile = '/home/astx/Desktop/Experiments/Anonim.Seq1.Ser3.Img1.dcm' #gotta be a dicom


disease_classes = ['Atelectasis', 'Pleural_Effusion', 'Edema']
results = [1 ,  0.123 , 0.4556 ]

def append_output2(dicomfile, disease_classes, results):  #dicomfile is a path, disease_classes, results are lists

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
    filedir, file, blank = dicomfile.rpartition(".dicom") ### uzantiya adaptif bir yapi uretme
    ds.save_as(filedir + "Radiologics" + file)              #Radiologics signature
