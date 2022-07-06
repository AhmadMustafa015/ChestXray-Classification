import pydicom as dicom
import os
import cv2
import PIL # optional
import numpy as np
import SimpleITK


# make it True if you want in PNG format
PNG = True
# Specify the .dcm folder path
folder_path = "C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\\vinbigdata-chest-xray-abnormalities-detection\\test"
# Specify the output jpg/png folder path
jpg_folder_path = "C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\VindataJPG\\Vin_test"
images_path = os.listdir(folder_path)
for n, image in enumerate(images_path):


    patient_path = os.path.join(folder_path, image)
    itk_img = SimpleITK.ReadImage(patient_path)
    photometric_interpretation = itk_img.GetMetaData('0028|0004').strip()
    print(photometric_interpretation)
    pixel_array_numpy = np.squeeze(SimpleITK.GetArrayFromImage(itk_img))
    '''
    image = SimpleITK.RescaleIntensity(image, 0, 255)
    if photometric_interpretation == 'MONOCHROME1':
        image = SimpleITK.InvertIntensity(image, maximum=255)
    image = SimpleITK.Cast(image, SimpleITK.sitkUInt8)
    '''
    '''
    data = pixel_array_numpy
    if photometric_interpretation == "MONOCHROME1":
        data = np.amax(data) - data
    data = data - np.min(data)
    data = data / np.max(data)
    data = (data * 255).astype(np.uint8)
    pixel_array_numpy = data
    '''
    '''
    addedvalue = np.max(pixel_array_numpy)
    pixel_array_numpy = pixel_array_numpy * -1
    pixel_array_numpy = pixel_array_numpy + addedvalue
    '''
    cv2.imwrite('color_img.jpg', pixel_array_numpy)
    cv2.imshow("image", pixel_array_numpy)
    cv2.waitKey()

    if PNG == False:
        image = image.replace('.dicom', '.jpg')
    else:
        image = image.replace('.dicom', '.png')
    cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
    if n % 50 == 0:
        print('{} image converted'.format(n))
    '''
    if photometric_interpretation == 'MONOCHROME1':
        image = image * -1 + max(image)
    pixel_array_numpy = np.squeeze(SimpleITK.GetArrayFromImage(itk_img))

    cv2.imwrite('color_img.jpg', pixel_array_numpy)
    cv2.imshow("image", pixel_array_numpy)
    cv2.waitKey()
    if PNG == False:
        image = image.replace('.dicom', '.jpg')
    else:
        image = image.replace('.dicom', '.png')
    cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
    if n % 50 == 0:
        print('{} image converted'.format(n))

'''
'''
### Uzantilari DICOM a cevirme, okunabilmesi icin
import os
import sys
#foldermain = 'D:/Datasets/Pulmonary Nodule/ICD-LNA/data/'
new_ext = '.dcm'
for folder in os.listdir(foldermain):
    for filename in os.listdir(foldermain + folder):
        infilename = os.path.join(foldermain + folder, filename)
        oldbase, extt = os.path.splitext(infilename)
        newnam = oldbase + new_ext
        output = os.rename(infilename, newnam)
        b =3
'''