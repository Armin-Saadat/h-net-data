import os
import glob
from tqdm import tqdm

from path_definition import CAP_DATA_DIR
from utils.others import read_nii_bysitk
from utils.patient import Patient

"""
0	Background
1   Myocardium
"""

if __name__ == '__main__':

    patients = {}
    for path in tqdm(glob.iglob(os.path.join(CAP_DATA_DIR, 'Training', 'img') + '**/*.nii.gz', recursive=True)):
        p_id = int(path.split('.nii.gz')[0].split('DET')[-1])
        img_path = os.path.join(CAP_DATA_DIR, 'Training', 'img', 'DET' + f'{p_id:07}' + '.nii.gz')
        label_path = os.path.join(CAP_DATA_DIR, 'Training', 'label', 'DET' + f'{p_id:07}' + '_seg.nii.gz')
        img = read_nii_bysitk(img_path)
        label = read_nii_bysitk(label_path)
        patients[p_id] = Patient(p_id, img[0], label[0])
