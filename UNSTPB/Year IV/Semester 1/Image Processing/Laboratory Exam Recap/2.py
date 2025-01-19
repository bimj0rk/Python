#%%

#b) Make an image that contains the magnitudes of the vertical edges of the object that has the lightest gray levels. 
#1. Segment the image so that you have the two labels: one for the object and one for the background. Visualize the segmented image with the appropriate vmin and vmax.

#import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color

#close all other images
plt.close('all')

#read the image and convert to grayscale
img = io.imread('tst2.bmp')
img = color.rgb2gray(img)
img = (img * 255).astype(int)

#show the original image
print('1)')
plt.figure()
plt.imshow(img, cmap = 'gray')

#get width and height of img
h, w = img.shape
hist,_ = np.histogram(img, range(0, 256))
plt.figure(figsize = (10, 10))
plt.plot(hist)

#compute the labes
img_labels = np.zeros((h, w))
img_labels[img < 175] = 0
img_labels[img >= 175] = 1

#show the segmented image
plt.figure()
plt.imshow(img_labels, cmap = 'gray', vmin = 0, vmax = 1)
plt.title("Segmented image")


#2) Extract only the vertical edges from the segmented image. Use the appropriate method considering the image is not noisy. Normalize the resulting image using the formula ((value - min) / (max - min)) * 255. Visualize the image with the contours with the appropriate vmin and vmax.

#vertical mask using gradient method
mask_vertical = np.array([[0, -1, 0], [0, 0, 0], [0, 1, 0]])

vert_edges = img.copy()
w_size = 3
border = w_size // 2

#apply the edge detection mask
for i in range(border, h - border):
    for j in range(border, w - border):
        V = img[i - border:i + border + 1, j - border:j + border + 1]
        V = V * mask_vertical
        vert_edges[i, j] = np.abs(np.sum(V))
        
#plot the figure
plt.figure()
plt.imshow(vert_edges, cmap = 'gray', vmin = 0, vmax = 1)
plt.title("Vertical edges")
# %%
