import os

from path_definition import SEGTHOR_DATA_DIR
from utils.others import read_nii_bysitk
from utils.patient import Patient

import numpy as np
import matplotlib.pyplot as plt

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

    for p in patients.values():
        p.print_data_shapes()

        slice_idx = 90

        for k in range(1, 5):
            b = np.copy(p.labels)
            b[np.where(p.labels == k)] = 1
            b[np.where(p.labels != k)] = 0

            fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 15))
            ax1.imshow(p.images[slice_idx], origin='lower', cmap='gray')
            ax2.imshow(p.labels[slice_idx], origin='lower', cmap='gray')
            ax3.imshow(b[slice_idx], origin='lower', cmap='gray')
            ax1.set_title("image")
            ax2.set_title("label")
            ax3.set_title(k)
            fig.show()
