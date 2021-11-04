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


# with open(os.path.join(SEGTHOR_DATA_DIR, 'images.pkl'), 'rb') as f:
#     images = pickle.load(f)
