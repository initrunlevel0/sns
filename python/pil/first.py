from PIL import Image

pil_im = Image.open('empire.jpg')

# color conversion to grayscale
grey_im = pil_im.conver('L')

# create thumbnail
thumb_im = pil_im.thumbnail((128,128))

# copy paste region
box = (100,100,400,400)
region_im = pil_im.crop(box)

# resize

resize_im = pil_im.resize((128, 128))

# rotate
rotate_im = pil_im.rotate(45)
