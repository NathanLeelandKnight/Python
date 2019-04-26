import numpy as np
import sys, random, argparse
from PIL import Image
import math

#70 levels of gray
gscale70 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

#10 levels of gray
gscale10 = "@%#*+=-:. "

if len(sys.argv) != 2:
	print("Please pass only one image file in as an argument!")

image = Image.open(sys.argv[1]).convert("L")

image.show()