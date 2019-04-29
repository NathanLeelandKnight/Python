import numpy as np
import sys, random, argparse
from PIL import Image
import math

#70 levels of gray
gscale70 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

#10 levels of gray
gscale10 = "@%#*+=-:. "

if len(sys.argv) != 4:
	print("Use program as: python ASCIIArt.py \'image.jpg\' \'#chars to use (10 or 70)\' \'#columns\'")
	exit()

scaleNum = int(sys.argv[2])
cols = int(sys.argv[3])

if 10 != scaleNum != 70:
	print("#chars to use needs to be 10 or 70")
	exit()

if not (0 < cols < 251):
	print("#columns must be between [1, 250]")
	exit()

image = Image.open(sys.argv[1]).convert("L")

W = image.size[0]
H = image.size[1]

scale = W / H
tileW = W / cols
tileH = tileW / scale

def getAverageL(image):
	im = np.array(image)
	w,h = im.shape
	return np.average(im.reshape(w*h))

