from PIL import Image
import numpy
import matplotlib.pyplot as plt

im = numpy.array(Image.open('empire.jpg'))

plt.imshow(im)

# point
x = [100,100,400,400]
y = [200,500,200,500]

plt.plot(x,y,'r*')  # r*: Red star mark

# lineplot
plt.plot(x[:2],y[:2])

# create new figure (with histogram)
plt.figure()
plt.hist(im.flatten(), 128)

# create new figure (with countour image)
plt.figure()
plt.gray()
plt.contour(Image.open('empire.jpg').convert('L'), origin='image') # convert('L') => greyscale


plt.show()
