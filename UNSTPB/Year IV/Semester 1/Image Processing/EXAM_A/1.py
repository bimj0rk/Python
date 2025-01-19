# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:50:48 2025

@author: Valentina
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import io,color

plt.close('all')

img=io.imread('lena.png')
img=color.rgb2gray(img)
img=(img*255).astype(int)

plt.figure(), plt.imshow(img, cmap='gray'), plt.colorbar()