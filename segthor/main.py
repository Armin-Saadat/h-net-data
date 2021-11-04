import os
import pickle

from path_definition import SEGTHOR_DATA_DIR
from utils.others import read_nii_bysitk
from utils.patient import Patient

"""
0	Background
1   Esophagus
2   Heart
3   Trachea
4   Aorta
"""

if __name__ == '__main__':

    patients = {}
    for p_id in range(1, 41):
        img_path = os.path.join(SEGTHOR_DATA_DIR, 'Training', 'Patient_' + f'{p_id:02}',
                                'Patient_' + f'{p_id:02}' + '.nii.gz')
        label_path = os.path.join(SEGTHOR_DATA_DIR, 'Training', 'Patient_' + f'{p_id:02}', 'GT.nii.gz')
        img = read_nii_bysitk(img_path)
        label = read_nii_bysitk(label_path)
        patients[p_id] = Patient(p_id, img, label)

    images = []
    labels = []
    for p in patients.values():
        p.normalize()
        images.append(p.images)
        labels.append(p.labels)

    with open(os.path.join(SEGTHOR_DATA_DIR, 'images.pkl'), 'wb') as f:
        pickle.dump(images, f)
    with open(os.path.join(SEGTHOR_DATA_DIR, 'labels.pkl'), 'wb') as f:
        pickle.dump(labels, f)

        # for k in range(1, 5):
        #     b = np.copy(p.labels)
        #     b[np.where(p.labels == k)] = 1
        #     b[np.where(p.labels != k)] = 0


