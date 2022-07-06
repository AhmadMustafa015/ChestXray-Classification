import glob
import pydicom
import SimpleITK as sitk
from append_output import append_output2
import os
from os import walk
import sys
import argparse
import logging
import json
import time
from easydict import EasyDict as edict
import torch
import numpy as np
from torch.utils.data import DataLoader
from torch.nn import DataParallel
import torch.nn.functional as F

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from data.dataset import ImageDataset  # noqa
from model.classifier import Classifier  # noqa

parser = argparse.ArgumentParser(description='Test model')

parser.add_argument('--model_path', default='./', metavar='MODEL_PATH',
                    type=str, help="Path to the trained models")
parser.add_argument('--in_csv_path', default='dev.csv', metavar='IN_CSV_PATH',
                    type=str, help="Path to the input image path in csv")
parser.add_argument('--out_csv_path', default='test/test_pacs_demo.csv',
                    metavar='OUT_CSV_PATH', type=str,
                    help="Path to the ouput predictions in csv")
parser.add_argument('--num_workers', default=2, type=int, help="Number of "
                    "workers for each data loader")
parser.add_argument('--device_ids', default='0', type=str, help="GPU indices "
                    "comma separated, e.g. '0,1' ")


def get_pred(output, cfg):
    if cfg.criterion == 'BCE' or cfg.criterion == "FL":
        for num_class in cfg.num_classes:
            assert num_class == 1
        pred = torch.sigmoid(output.view(-1)).cpu().detach().numpy()
    elif cfg.criterion == 'CE':
        for num_class in cfg.num_classes:
            assert num_class >= 2
        prob = F.softmax(output)
        pred = prob[:, 1].cpu().detach().numpy()
    else:
        raise Exception('Unknown criterion : {}'.format(cfg.criterion))

    return pred


def test_epoch(cfg, args, model, dataloader, out_csv_path):
    torch.set_grad_enabled(False)
    model.eval()
    device_ids = list(map(int, args.device_ids.split(',')))
    device = torch.device('cuda:{}'.format(device_ids[0]))
    steps = len(dataloader)
    dataiter = iter(dataloader)
    num_tasks = len(cfg.num_classes)

    test_header = [
        'Path',
        'Cardiomegaly',
        'Edema',
        'Consolidation',
        'Atelectasis',
        'Pleural Effusion']

    with open(out_csv_path, 'w') as f:
        f.write(','.join(test_header) + '\n')
        for step in range(steps):
            image, path = next(dataiter)
            image = image.to(device)
            output, __ = model(image)
            batch_size = len(path)
            pred = np.zeros((num_tasks, batch_size))

            for i in range(num_tasks):
                pred[i] = get_pred(output[i], cfg)

            for i in range(batch_size):
                batch = ','.join(map(lambda x: '{}'.format(x), pred[:, i]))
                result = path[i] + ',' + batch
                f.write(result + '\n')
                logging.info('{}, Image : {}, Prob : {}'.format(
                    time.strftime("%Y-%m-%d %H:%M:%S"), path[i], batch))



def run(args):

    #### CREATE THE CSV FROM THE IMAGES FOLDER (JPG)

    csv_path = 'C:\\Users\\RadioscientificOne\PycharmProjects\Aphrodite\\pacs_demo.csv'
    image_folder = 'C:\\Users\\RadioscientificOne\\PycharmProjects\\Aphrodite\\PACS_DEMO\\'
    test_header = 'Path,Sex,Age,Frontal/Lateral,AP/PA,No Finding,Enlarged Cardiomediastinum,Cardiomegaly,Lung Opacity,' \
                  'Lung Lesion,Edema,Consolidation,Pneumonia,Atelectasis,Pneumothorax,Pleural Effusion,Pleural Other,' \
                  'Fracture,Support Devices'
    '''
    _, _, filenames = next(walk(image_folder))

    with open(csv_path, 'w') as f:
        f.write(test_header + '\n')
        for i in filenames:
            f.write(image_folder + i + ',' + '\n')
    '''
    args = parser.parse_args()
    args.model_path = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\\config\\'
    args.in_csv_path = csv_path
    args.out_csv_path = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\CheXpert\Chexpert\\bin\\test\\test_pacs_demo.csv'

    ########## TEST MODEL RUN ON CUSTOM IMAGES
    with open(args.model_path + 'example.json') as f:
        cfg = edict(json.load(f))

    device_ids = list(map(int, args.device_ids.split(',')))
    num_devices = torch.cuda.device_count()
    if num_devices < len(device_ids):
        raise Exception(
            '#available gpu : {} < --device_ids : {}'
            .format(num_devices, len(device_ids)))
    device = torch.device('cuda:{}'.format(device_ids[0]))

    model = Classifier(cfg)
    model = DataParallel(model, device_ids=device_ids).to(device).eval()
    ckpt_path = os.path.join(args.model_path, 'best1.ckpt')
    ###
    #ckpt_path1 = 'C:\\Users\\me\\PycharmProjects\\CheXpert\\Chexpert\\config\\pre_train.pth'
    ckpt_path1 = 'C:\\Users\\RadioscientificOne\\PycharmProjects\\Aphrodite\\CheXpert\\Chexpert\\config\\pre_train.pth'
    ckpt = torch.load(ckpt_path1, map_location=device)
    ###
    #ckpt = torch.load(ckpt_path, map_location=device)
    #model.module.load_state_dict(ckpt['state_dict'])
    model.module.load_state_dict(ckpt)

    ### batch size degistirilio
    b = args.in_csv_path
    dataloader_test = DataLoader(
        ImageDataset(args.in_csv_path, cfg, mode='test'),
        batch_size=1, num_workers=args.num_workers,
        drop_last=False, shuffle=False)

    test_epoch(cfg, args, model, dataloader_test, args.out_csv_path)

    #### DICOM MODIFIYE EDILMIS SEKILDE KAYDEDILMESI
    root_dicom_path = 'C:\\Users\RadioscientificOne\PycharmProjects\Aphrodite\\vinbigdata-chest-xray-abnormalities-detection\\train\\'
    with open(args.out_csv_path) as f:
        header = f.readline()
        for line in f:
            fields = line.strip('\n').split(',')
            base_name = os.path.basename(fields[0])
            dicom_name = os.path.splitext(base_name)[0]
            dicom_full_path = root_dicom_path + dicom_name + '.dicom'
            #############  KODUN DEVAMI VE YENILENMIS HALI JPEG2DICOM PROJESINDE (ENVIRONMENT DOLAYI)






def main():
    logging.basicConfig(level=logging.INFO)

    args = parser.parse_args()
    run(args)
if __name__ == '__main__':
    main()


'''
#cardiomegaly ornegi
patient_cmegaly = '00aca42a24e4ea6066cca2546150c36e'
jpeg_path = '/VinBigJPG/train/train\\'
dcm_path = '/vinbigdata-chest-xray-abnormalities-detection/train\\'

dcm_patient_path = os.path.join(dcm_path,patient_cmegaly) + '.dicom'
ds = pydicom.filereader.dcmread(dcm_patient_path)
print(ds)

disease_classes = ['Atelectasis', 'Cardiomegaly', 'Consolidation', 'Pleural_Effusion', 'Edema']
results = [0.26 ,  0.9 , 0.456 , 0.54 , 0.39 ]

#append_output2(dcm_patient_path,disease_classes,results)
'''










'''
reader = sitk.ImageSeriesReader()
# Use the functional interface to read the image series.
itk_img = sitk.ReadImage(reader.GetGDCMSeriesFileNames(dcm_path, patient_cmegaly))
img_array = sitk.GetArrayFromImage(itk_img)
dicom_names = reader.GetGDCMSeriesFileNames(dcm_patient_path)
a =1
'''