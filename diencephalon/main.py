import os

from path_definition import DIENCEPHALON_DATA_DIR
from utils.others import read_nii_bysitk
from utils.patient import Patient

"""
0	Background
23	Right Accumbens Area
30	Left Accumbens Area
31	Right Amygdala
32	Left Amygdala
36	Right Caudate
37	Left Caudate
47	Right Hippocampus
48	Left Hippocampus
55	Right Pallidum
56	Left Pallidum
57	Right Putamen
58	Left Putamen
59	Right Thalamus Proper
60	Left Thalamus Proper
"""

if __name__ == '__main__':
    patient_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 23, 24, 25, 36, 38, 39, 101, 104,
                   107, 110, 113, 116, 119, 122, 125, 128]

    patients = {}
    for p_id in patient_ids:
        img_path = os.path.join(DIENCEPHALON_DATA_DIR, 'Training', 'img', '1' + f'{p_id:03}' + '_3.nii.gz')
        label_path = os.path.join(DIENCEPHALON_DATA_DIR, 'Training', 'label', '1' + f'{p_id:03}' + '_3_glm.nii.gz')
        img = read_nii_bysitk(img_path)
        label = read_nii_bysitk(label_path)
        patients[p_id] = Patient(p_id, img, label)

    for p in patients.values():
        p.print_data_shapes()
