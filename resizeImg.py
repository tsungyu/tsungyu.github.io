import sys
sys.path.append("/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python")
from cv2 import imread as imread
from cv2 import resize as imresize
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

for f in os.listdir('ProjectThumbnail'):
    extension = os.path.splitext(f)[1]
    if extension not in ['.png', '.jpg']:
        continue
    img = imread(os.path.join('ProjectThumbnail', f))
    img = imresize(img, (300, 200))

    cv2.imwrite(os.path.join('thumbnail', f), img)




