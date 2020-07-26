from os import listdir, rename, makedirs, walk
from os.path import isfile, join

imgs_imgs_path = "./imgs/imgs"  # selected images path
masks_path = "./masks"
# get all selected images names
target_files = [f for f in listdir(imgs_imgs_path) if isfile(join(imgs_imgs_path, f))]
# convert the list to set
target_set = set(target_files)
# generate a corresponding selected masks path inside ./data/masks
masks_masks_path = join(masks_path, 'masks')

try:
    makedirs(masks_masks_path)
except:
    pass

for _, _, f in walk(masks_path):
    for file in f:
        if file in target_set:
            # move masks files from ./data/masks to ./data/masks/masks
            rename(join(masks_path, file), join(masks_masks_path, file))

print('Done')
