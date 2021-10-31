import SimpleITK as sitk


def read_nii_bysitk(input_fid, peel_info=False):
    """ read nii to numpy through simpleitk
        peelinfo: taking direction, origin, spacing and metadata out
    """
    img_obj = sitk.ReadImage(input_fid)
    img_np = sitk.GetArrayFromImage(img_obj)
    if peel_info:
        info_obj = {
            "spacing": img_obj.GetSpacing(),
            "origin": img_obj.GetOrigin(),
            "direction": img_obj.GetDirection(),
            "array_size": img_np.shape
        }
        return img_np, info_obj
    else:
        return img_np


# def save_patients_images(path):
#     images = {}
#     for id, patient in patients.items():
#         images[id] = patient.images
#     with open(path, 'wb') as f:
#         pickle.dump(images, f)


# def save_patients_labels(path):
#     labels = {}
#     for id, patient in patients.items():
#         labels[id] = patient.labels
#     with open(path, 'wb') as f:
#         pickle.dump(labels, f)


# def save_patients_superpixs(path):
#     superpixs = {}
#     for id, patient in patients.items():
#         superpixs[id] = patient.superpixs
#     with open(path, 'wb') as f:
#         pickle.dump(superpixs, f)
