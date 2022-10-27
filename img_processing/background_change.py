from rembg import remove
from PIL import Image
import os

in_path = 'img_processing/images/input/'
out_path = 'img_processing/images/output/'

for root, dirs, files in os.walk(in_path):    
    for name in files:
        input_path = root + name
        output_path = out_path + name.split('.')[0] + '.png'     

        input = Image.open(input_path)
        output = remove(input)
        output.save(output_path)
