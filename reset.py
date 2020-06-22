#Reset
#William Doyle

import matplotlib.image as img
import numpy as npy

#definitions
targetImg = img.imread('target.png')
width, height = targetImg.shape[:2]

#resetting alpha channel to opaque
for i in range(width):
    for j in range(height):
        targetImg[i][j][3] = 1

img.imsave('target.png', targetImg)
