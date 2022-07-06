import os
import cv2
import PIL # optional
import numpy as np
import SimpleITK as sitk

#input_file_name = "C:/Users/RadioscientificOne/PycharmProjects/Aphrodite/vinbigdata-chest-xray-abnormalities-detection/test/00b7e6bfa4dc1fe9ddd0ce74743e38c2.dicom"
#output_file_name = "C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite/"
## BOZUKLAR
# 03da4593b25a2e0095170197050cb551
# 0171021638f9272a34a41feb84ed47a0
# 0403dda5a9bf46457517b604869d530d



folder_path = "C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\\vinbigdata-chest-xray-abnormalities-detection\\test"
# Specify the output jpg/png folder path
jpg_folder_path = "C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\VindataJPG\\Vin_test"
images_path = os.listdir(folder_path)
for n, image11 in enumerate(images_path):

    patient_path = os.path.join(folder_path, image11)

    image_file_reader = sitk.ImageFileReader()
    image_file_reader.SetImageIO('GDCMImageIO')
    image_file_reader.SetFileName(patient_path)
    image_file_reader.ReadImageInformation()
    image = image_file_reader.Execute()

    if image.GetNumberOfComponentsPerPixel() == 1:
        image = sitk.RescaleIntensity(image, 0, 255)
        pixel_array_numpy1 = np.squeeze(sitk.GetArrayFromImage(image))
        if image_file_reader.GetMetaData('0028|0004').strip() == 'MONOCHROME1':
            print(image11)
        '''
        if image_file_reader.GetMetaData('0028|0004').strip() == 'MONOCHROME1':
            image = sitk.InvertIntensity(image, maximum=255)
            pixel_array_numpy2 = np.squeeze(sitk.GetArrayFromImage(image))
        '''
        image = sitk.Cast(image, sitk.sitkUInt8)
        pixel_array_numpy3 = np.squeeze(sitk.GetArrayFromImage(image))


    image11 = image11.replace('.dicom', '.png')
    output_file_name = os.path.join(jpg_folder_path, image11)
    sitk.WriteImage(image, output_file_name)

    if n % 50 == 0:
        print('{} image converted'.format(n))