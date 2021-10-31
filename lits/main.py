import os

from path_definition import LITS_DATA_DIR
from utils.others import read_nii_bysitk
from utils.patient import Patient

"""
0	Background
1   Liver
2   Lesion
"""

if __name__ == '__main__':

    patients = {}
    for p_id in range(28):
        img_path = os.path.join(LITS_DATA_DIR, 'Training', 'img', 'volume-' + str(p_id) + '.nii.gz')
        label_path = os.path.join(LITS_DATA_DIR, 'Training', 'label', 'segmentation-' + str(p_id) + '.nii.gz')
        img = read_nii_bysitk(img_path)
        label = read_nii_bysitk(label_path)
        patients[p_id] = Patient(p_id, img, label)

    for p in patients.values():
        p.print_data_shapes()
