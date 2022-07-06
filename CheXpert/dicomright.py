import numpy as np
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
import os
import cv2
import PIL # optional
import numpy as np
import matplotlib.pyplot as plt


def read_xray(path, voi_lut=True, fix_monochrome=True):
    dicom = pydicom.read_file(path)

    # VOI LUT (if available by DICOM device) is used to transform raw DICOM data to "human-friendly" view
    if voi_lut:
        data = apply_voi_lut(dicom.pixel_array, dicom)
    else:
        data = dicom.pixel_array

    # depending on this value, X-ray may look inverted - fix that:
    if fix_monochrome and dicom.PhotometricInterpretation == "MONOCHROME1":
        data = np.amax(data) - data

    data = data - np.min(data)
    data = data / np.max(data)
    data = (data * 255).astype(np.uint8)

    return data

#img = read_xray('../input/vinbigdata-chest-xray-abnormalities-detection/train/0108949daa13dc94634a7d650a05c0bb.dicom')
#plt.figure(figsize = (12,12))
#plt.imshow(img, 'gray')

folder_path = "C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\\vinbigdata-chest-xray-abnormalities-detection\\test"
# Specify the output jpg/png folder path
jpg_folder_path = "C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\VindataJPG\\Vin_testdene"
images_path = os.listdir(folder_path)
for n, image in enumerate(images_path):
    patient_path = os.path.join(folder_path, image)
    img = read_xray(patient_path)

    cv2.imwrite('color_img.jpg', img)
    cv2.imshow("image", img)
    cv2.waitKey()
    #plt.figure(figsize=(12, 12))
    #plt.imshow(img, 'gray')
