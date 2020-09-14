from os import listdir, rename, makedirs, walk
from os.path import isfile, join

mask_path = "./120"  # selected images path
img_path = "./left_imgs"
# get all selected images names
target_files = [f for f in listdir(mask_path) if isfile(join(mask_path, f))]
# convert the list to set
target_set = set(target_files)
# generate a corresponding selected masks path inside ./data/masks
new_img_path = join(".", 'new_imgs')

try:
    makedirs(new_img_path)
except:
    pass

for _, _, f in walk(img_path):
    for file in f:
        if file in target_set:
            # move masks files from ./data/masks to ./data/masks/masks
            rename(join(img_path, file), join(new_img_path, file))

print('Done')
