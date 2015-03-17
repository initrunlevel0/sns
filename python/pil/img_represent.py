from PIL import Image
from matplotlib.pyplot import *
import numpy

im = numpy.array(Image.open('empire.jpg'))

print im.shape, im.dtype

# output:
# (800, 569, 3) uint8

# print all array
print im

# graylevel transforms
im2 = 255 - im
im3 = (100.0/255) * im + 100 # clamp to interval 100..200
im4 = 255.0 * (im/255.0)**2 # squared

#imshow(im2)

#figure()
#imshow(im3)
#figure()
#imshow(im4)
#show()


# Histogram Equalization
# Oops, Histogram dalam statistik berarti diagram yang menampilkan distribusi dari nilai tertentu
# Dalam konteks Image Processing, nilai yang dilihat distribusinya adalah "warna"


