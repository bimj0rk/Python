#%%

#a) Convert the image to grayscale and visualize the result using the appropriate functions and colormap.

#necesary libraries
from skimage import io, color
import matplotlib.pyplot as plt

#close all other images
plt.close('all')

#read the image
img_original = io.imread('lena.png')

#convert the image to grayscale
img_gray = color.rgb2gray(img_original)

#show the image
plt.figure()
plt.imshow(img_gray, cmap = 'gray')
plt.colorbar()
# %%
