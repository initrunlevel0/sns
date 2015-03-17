from PIL import Image
from numpy import *

im = array(Image.open('./empire.jpg').conver('L'))
im2, cdf = imtools.histeq(im)
