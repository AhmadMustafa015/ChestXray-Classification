import os
import cv2
import PIL # optional
import numpy as np
import SimpleITK as sitk

input_file_name = "C:/Users/RadioscientificOne/PycharmProjects/Aphrodite/vinbigdata-chest-xray-abnormalities-detection/test/03da4593b25a2e0095170197050cb551.dicom"
output_file_name = "C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite/bozuknasil.png"
## BOZUKLAR
# 03da4593b25a2e0095170197050cb551
# 0171021638f9272a34a41feb84ed47a0
# 0403dda5a9bf46457517b604869d530d


image_file_reader = sitk.ImageFileReader()
image_file_reader.SetImageIO('GDCMImageIO')
image_file_reader.SetFileName(input_file_name)
image_file_reader.ReadImageInformation()
image = image_file_reader.Execute()
pixel_array_numpy = np.squeeze(sitk.GetArrayFromImage(image))
maxdeger = np.max(pixel_array_numpy)
mindeger = np.min(pixel_array_numpy)

if image.GetNumberOfComponentsPerPixel() == 1:
    image = sitk.RescaleIntensity(image, 0, 255)
    pixel_array_numpy1 = np.squeeze(sitk.GetArrayFromImage(image))
    if image_file_reader.GetMetaData('0028|0004').strip() == 'MONOCHROME1':
        print(image11)

    if image_file_reader.GetMetaData('0028|0004').strip() == 'MONOCHROME1':
        image = sitk.InvertIntensity(image, maximum=255)
        pixel_array_numpy2 = np.squeeze(sitk.GetArrayFromImage(image))

    image = sitk.Cast(image, sitk.sitkUInt8)
    pixel_array_numpy3 = np.squeeze(sitk.GetArrayFromImage(image))


#image11 = image11.replace('.dicom', '.png')
#output_file_name = os.path.join(jpg_folder_path, image11)
sitk.WriteImage(image, output_file_name)

