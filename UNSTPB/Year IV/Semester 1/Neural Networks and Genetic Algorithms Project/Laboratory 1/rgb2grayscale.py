#%%
import numpy as np
import matplotlib.pyplot as plt

img_original = plt.imread('like.jpg')
plt.imshow(img_original)
plt.show()

img_grayscale = 0.299 * img_original[:, :, 0] + 0.587 * img_original[:, :, 1] + 0.114 * img_original[:, :, 2]
plt.imshow(img_grayscale, cmap = 'gray')
plt.savefig("grayscaled.jpg")
plt.show()

#why the sum of these coeffs should be one?
# %%
