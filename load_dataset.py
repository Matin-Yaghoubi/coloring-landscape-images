import os
from PIL import Image
import numpy as np

def load_data(image_dir, size) :
    gray_dir  = f'{image_dir}/gray'
    color_dir  = f'{image_dir}/color'

    img_size = (size , size)

    grays = []
    colors = []

    for name in sorted(os.listdir(gray_dir)):
        file_path = os.path.join(gray_dir , name)
        img = Image.open(file_path)
        img = img.resize(img_size)
        img = np.array(img)/255
        grays.append(img)

    for name in sorted(os.listdir(color_dir)):
        file_path = os.path.join(color_dir , name)
        img = Image.open(file_path)
        img = img.convert('RGB')
        img = img.resize(img_size)
        img = np.array(img)/255
        colors.append(img)

    return grays, colors