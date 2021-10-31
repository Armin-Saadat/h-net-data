import os

from path_definition import SABS_DATA_DIR
from utils.others import read_nii_bysitk
from utils.patient import Patient

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
        img = read_nii_bysitk(img_path)
        label = read_nii_bysitk(label_path)
        patients[p_id] = Patient(p_id, img, label)

    for p in patients.values():
        p.print_data_shapes()
