# -*- coding: utf-8 -*-
"""
Demo script to go along with a Python tutorial @ BIG (EPFL). 
http://naereen.github.io/slides/2016_07__Python_demo_at_EPFL/


- Author: Lilian Besson
- Date: 07 July 2016
- License: MIT License (http://lbesson.mit-license.org/)
- GitHub: http://naereen.github.io/slides/2016_07__Python_demo_at_EPFL/
"""


# %% First example
print("Hello Python world!")
# Hello Python world!


# %% Graphical example 1
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 400)
x = np.cos(2*t)
y = np.cos(3*t)
plt.figure()
plt.plot(x, y, 'r+-')
plt.show()


# %% Graphical example 2
from scipy.special import gamma
x = np.linspace(0.1, 3, 400)
y = gamma(x)
plt.figure()
plt.plot(x, y)
plt.title("The function $\Gamma(x)$ on $[0.1, 3]$")
plt.show()


# %% Reading an image
from scipy import ndimage  # module for n-d images
import matplotlib.pyplot as plt  # module for plotting

from scipy import misc  # some toy data are in this module
face = misc.face()
# Or...
# face = plt.imread('face.png')
# Or...
from skimage.io import imread  # import a function
# face = imread('face.jpg')

print(face[0, 0])  # first pixel: 114
# display the image
plt.imshow(face, cmap='gray')
plt.show()


# %% More on images
lx, ly = face.shape
# cropping, by slicing the ndarray (matrix)
crop_face = face[lx / 4: - lx / 4, ly / 4: - ly / 4]
# up <-> down flip
flip_ud_face = np.flipud(face)
# rotation
rotate_face = ndimage.rotate(face, 45)
rotate_face_noreshape = ndimage.rotate(face, 45, reshape=False)

plt.figure()
plt.subplot(2, 3, 1)
plt.imshow(face, cmap='gray')
plt.subplot(2, 3, 2)
plt.imshow(crop_face, cmap='gray')
plt.subplot(2, 3, 3)
plt.imshow(flip_ud_face, cmap='gray')
plt.subplot(2, 3, 4)
plt.imshow(rotate_face, cmap='gray')
plt.subplot(2, 3, 5)
plt.imshow(rotate_face_noreshape, cmap='gray')
 