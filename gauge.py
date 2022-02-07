import argparse
import cv2
import os

from pycoral.adapters.common import input_size
from pycoral.adapters.detect import get_objects
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter
from pycoral.utils.edgetpu import run_inference
import PIL

from PIL import Image

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
