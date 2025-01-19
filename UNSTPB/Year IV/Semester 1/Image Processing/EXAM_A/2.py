# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:03:37 2024

@author: Rodcris
"""
from skimage import io,color,util 
import numpy as np
import matplotlib.pyplot as plt

#1

plt.close('all')

img = io.imread('tst2.bmp')
img = color.rgb2gray(img)
img = np.uint8(img*255).astype(int)

plt.figure(), plt.imshow(img,cmap='gray'), plt.colorbar(), plt.title("Original Image")
h, w=img.shape

img_labels = np.zeros([h,w])

img_labels[img<175]=0
img_labels[img>=175]=1

plt.figure(), plt.imshow(img_labels, cmap='gray',vmin = 0, vmax = 1), plt.colorbar(), plt.title("Segmented Image")

#2
mask_vert=np.array([[0,-1,0],
                 [0,0,0],
                 [0,1,0]])


img_fvert=img.copy()
w_size=3
border=w_size//2

for i in range(border, h-border):
    for j in range(border, w-border):
        V=img_labels[i-border:i+border+1, j-border:j+border+1]
        V_vert=V*mask_vert
        img_fvert[i,j]=np.abs(np.sum(V_vert))
        
plt.figure(), plt.imshow(img_fvert, cmap='gray', vmin=0, vmax=1), plt.colorbar(), plt.title("Vertical Edge Image")