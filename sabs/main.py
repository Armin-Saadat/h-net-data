import os
import pickle

from path_definition import SABS_DATA_DIR
from utils.others import read_nii_bysitk
from utils.patient import Patient

import numpy as np

"""
(0)	Background
(1) spleen
(2) right kidney
(3) left kidney
(4) gallbladder
(5) esophagus
(6) liver
(7) stomach
(8) aorta
(9) inferior vena cava
(10) portal vein and splenic vein
(11) pancreas
(12) right adrenal gland
(13) left adrenal gland
"""

if __name__ == '__main__':
    patient_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
                   38, 39, 40]

    patients = {}
    for p_id in patient_ids:
        img_path = os.path.join(SABS_DATA_DIR, 'Training', 'img', 'img' + f'{p_id:04}' + '.nii.gz')
        label_path = os.path.join(SABS_DATA_DIR, 'Training', 'label', 'label' + f'{p_id:04}' + '.nii.gz')
        img = read_nii_bysitk(img_path).astype(np.float32)
        label = read_nii_bysitk(label_path).astype(np.float32)
        patients[p_id] = Patient(p_id, img, label)

    images = []
    labels = []
    for p in patients.values():
        p.remove_paddings()
        p.resize((256, 256))
        p.normalize()
        images.append(p.images)
        labels.append(p.labels)

    with open(os.path.join(SABS_DATA_DIR, 'images.pkl'), 'wb') as f:
        pickle.dump(images, f)
    with open(os.path.join(SABS_DATA_DIR, 'labels.pkl'), 'wb') as f:
        pickle.dump(labels, f)
