from os import listdir
from os.path import isfile, join

from PIL import Image

imgs_path = "../120_person/imgs"
target_files = [f for f in listdir(imgs_path) if isfile(join(imgs_path, f)) and not f.startswith('.')]
for file in target_files:
    grey_img = join(imgs_path, file)
    img = Image.open(grey_img)
    if img.mode == "LA":
        new_img = img.convert('L')
        new_img.save(grey_img)

print("Done")
