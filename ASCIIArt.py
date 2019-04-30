import numpy as np
import sys, random, argparse
from PIL import Image
import math

#70 levels of gray
gscale70 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

#10 levels of gray
gscale10 = "@%#*+=-:. "

def getAverageL(image):
	im = np.array(image)
	w,h = im.shape
	return np.average(im.reshape(w*h))

if len(sys.argv) != 6:
	print("Use program as: python ASCIIArt.py \'image.jpg\' \'#chars to use (10 or 70)\' \'#columns\' \'vertical scale\' \'outfile location\'")
	exit()

gScaleNum = int(sys.argv[2])
cols      = int(sys.argv[3])
vertScale = float(sys.argv[4])
outFile   = sys.argv[5]

if 10 != gScaleNum != 70:
	print("#chars to use needs to be 10 or 70")
	exit()

if not (0 < cols < 351):
	print("#columns must be between [1, 350]")
	exit()

if not (0 < vertScale < 11):
	print("vertical scale must be between [1, 10]")

image = Image.open(sys.argv[1]).convert("L")

W = image.size[0]
H = image.size[1]
w = W / cols
h = w / vertScale

rows  = int(H / h)


aimg = []

for i in range(rows):
	y1 = int(i*h)
	y2 = int((i+1)*h)

	if i == (rows - 1):
		y2 = H

	aimg.append("")

	for j in range(cols):
		x1 = int(j*w)
		x2 = int((j+1)*w)

		if j == (cols - 1):
			x2 = W

		img = image.crop((x1, y1, x2, y2))
		avg = int(getAverageL(img))

		if gScaleNum == 10:
			gval = gscale10[int((avg*9)/255)]
		else:
			gval = gscale70[int((avg*69)/255)]

		aimg[i] += gval

f = open(outFile, 'w')

for row in aimg:
	f.write(row + '\n')
f.close()

