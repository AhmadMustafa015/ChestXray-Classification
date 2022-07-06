import pydicom as dicom
import os
import SimpleITK
import cv2

denem = 'C:\\Users\\RadioscientificOne\\PycharmProjects\\Aphrodite\\vinbigdata-chest-xray-abnormalities-detection\\test\\002a34c58c5b758217ed1f584ccbcfe9.dicom'
#ds = dicom.read_file(denem)
itk_img = SimpleITK.ReadImage(denem)
img_array = SimpleITK.GetArrayFromImage(itk_img)
#aaa = ds.pixel_array
a=0



folder_path = "C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\\vinbigdata-chest-xray-abnormalities-detection\\test"
images_path = os.listdir(folder_path)

for n, image in enumerate(images_path):

    patient_path = os.path.join(folder_path, image)
    ds = dicom.read_file(patient_path)
    try:
        pixel_array_numpy = ds.pixel_array
    except:
        print(image)


























