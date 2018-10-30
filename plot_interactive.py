import matplotlib.pyplot as plt
from PIL import Image
im1_path = 'images/girl2.jpg'
im2_path = 'images/timg2.jpg'

im1 = Image.open(im1_path)
im2 = Image.open(im2_path)

plt.ion()
plt.figure()
plt.imshow(im1)
plt.figure()
plt.imshow(im2)
plt.ioff()

plt.show()