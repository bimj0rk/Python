#%%

#S4. Let be the image test1.jpg with 256 graylevels.
#a. Read the image, convert it to grayscale and visualize it with the correct colormap.

#necessary modules
import matplotlib.pyplot as plt
from skimage import io, color
import numpy as np
import matplotlib as mpl

plt.close('all')

#read the image
img_orig = io.imread('test1.jpg')

#convert to grayscale
img_gray = color.rgb2gray(img_orig)

#visualize the image
plt.figure()
plt.imshow(img_gray, cmap = 'gray')
plt.colorbar()


#b. The image contains noise inside the objects. Filter the image with the appropriate filter to reduce the noise. Visualize the result. (for bonus points, filter only inside the object)
#I will use a median filter, since the noise is non linear

img_to_be_filtered = img_gray.copy()
img_to_be_filtered = np.uint(img_to_be_filtered * 255) #convert to 0...255 from 0..1, since it was 'deconverted' when converted to grayscale
img_filtered = img_gray.copy()
h, w = img_to_be_filtered.shape #compute height and width

#for each pixel in the image, select the middle of the 3x3 neighbourhood value range and replace it in the original image
for i in range(1, h - 1):
    for j in range(1, w - 1):
        V = img_to_be_filtered[i - 1:i + 2, j - 1:j + 2]
        V = V = np.sort(V, axis = None)
        img_filtered[i, j] = V[4]

#show the image
plt.figure()
plt.imshow(img_filtered, cmap = 'gray')
plt.colorbar()


#c. Make a colormap with pure red, pure green, dark blue and white evenly spaces. Visualize the image with this colormap. Explain the result.
img_to_be_seen = img_filtered.copy()

#colormap definition
colormap = np.zeros([256, 3])

#adding pure red to the colormap
for i in range (64):
    colormap[i, 0] = 1 #R
    
#adding pure green to the colormap
for i in range(64, 128):
    colormap[i, 0] = 0 #R
    colormap[i, 1] = 1 #G
    
#adding dark blue to the colormap
for i in range(128, 192):
    colormap[i, 0] = 0 #R
    colormap[i, 1] = 0 #G
    colormap[i, 2] = 0.5 #B, value for dark blue
    
#adding white to the colormap
for i in range(192, 256):
    colormap[i, 0] = 1 #R
    colormap[i, 1] = 1 #G
    colormap[i, 2] = 1 #B
    
colormap = mpl.colors.ListedColormap(colormap) #create the colormap
    
#visualizing the image using this colormap
plt.figure()
plt.imshow(img_to_be_seen, cmap = colormap)
plt.colorbar()

'''
in the original photo, in the middle bar, corresponding to
the gray-ish color, a gradient can be seen, as well as in the
circle on the right, and that explains the sudden change in
color (there is a sudden change in the colormap)
'''


#d. Filter the original image with a filter that works on a 3x3 centered neighbourhood and does the difference between the current pixel and the mean of the following ones: the pixel above, the pixel below, the pixel at the right and the pixel at the left of the origin (current pixel).
#Out = current pixel - mean(top, bottom, left, right). Visualize the filtered images with the appropriate vmin and vmax.
img_to_be_filtered_2 = img_gray.copy()
img_to_be_filtered_2 = np.uint(img_to_be_filtered_2 * 255)
h_1, w_1 = img_to_be_filtered_2.shape

#define the mask for a 3x3 neighbourhood
mask_size = 3
mask = [[0, 1 ,0], [1, 0 ,1], [0, 1, 0]]#top, left, right, bottom pixels kernel

img_filtered_2 = np.zeros([h_1, w_1])#generate an empty image
 
#for each pixel in the mask, compute the mean of the neighbouring pixels and substract it from the current pixel
for i in range(mask_size // 2, h_1 - mask_size // 2):
    for j in range(mask_size // 2, w_1 - mask_size // 2): 
        V = img_to_be_filtered_2[i - mask_size//2:i + mask_size//2 + 1, j - mask_size//2:j + mask_size//2 + 1]
        V = V * mask
        img_filtered_2[i, j] = img_to_be_filtered_2[i, j] - np.mean(V)
        
#visualize the image
plt.figure()
plt.imshow(img_filtered_2, cmap = 'gray', vmin = 0, vmax = 256)
plt.colorbar()
# %%
