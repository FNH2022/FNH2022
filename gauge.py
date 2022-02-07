import os
import pathlib
from pycoral.utils import edgetpu
from pycoral.utils import dataset
from pycoral.adapters import common
from pycoral.adapters import classify
from PIL import Image

import PIL


percent = 70  
output_file_name = 'new_gauge.png'
x = 825
y = 825
loc = (x, y)

percent = percent / 100
rotation = 180 * percent  
rotation = 90 - rotation  
dial = Image.open('needle.png')
dial = dial.rotate(rotation, resample=PIL.Image.BICUBIC, center=loc)  

gauge = Image.open('gauge.png')
gauge.paste(dial, mask=dial)  
gauge.save(output_file_name)
