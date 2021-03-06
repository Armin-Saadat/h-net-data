import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize


class Patient:
    def __init__(self, id_, img, label):
        self.id = id_
        assert img.shape == label.shape, 'image and label should have the same shape.'
        self.slice_n = img.shape[0]
        self.size = img.shape[1:]
        self.images = img
        self.labels = label

    def remove_without_labels(self):
        idx = []
        for slice_idx, label in enumerate(self.labels):
            if label.max() > 0:
                idx.append(slice_idx)
        self.slice_n = len(idx)
        self.images = self.images[idx]
        self.labels = self.labels[idx]

    def remove_paddings(self):
        idx = []
        for slice_idx, img in enumerate(self.images):
            if img.max() > 0:
                idx.append(slice_idx)
        self.slice_n = len(idx)
        self.images = self.images[idx]
        self.labels = self.labels[idx]

    def normalize(self):
        min_ = self.images.min()
        max_ = self.images.max()
        for slice_idx, img in enumerate(self.images):
            self.images[slice_idx] = (img - min_) / (max_ - min_)

    def resize(self, output_shape):
        self.images = resize(self.images, (self.slice_n, output_shape[0], output_shape[1]), anti_aliasing=True)
        self.labels = resize(self.labels, (self.slice_n, output_shape[0], output_shape[1]), anti_aliasing=False).astype(
            int).astype(np.float32)

    def print_data_shapes(self):
        print('p_id:', self.id)
        print('images: ', self.images.shape)
        print('labels: ', self.labels.shape)
        print('-' * 30)

    def plot(self, slice_idx):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 15))
        ax1.imshow(self.images[slice_idx], origin='lower', cmap='gray')
        ax2.imshow(self.labels[slice_idx], origin='lower', cmap='gray')
        ax1.set_title("image")
        ax2.set_title("label")
        fig.show()
