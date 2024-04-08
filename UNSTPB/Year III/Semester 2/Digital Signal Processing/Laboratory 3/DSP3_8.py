import numpy as np
import scipy.signal as sp

h = np.array([1, 1, 1])
x = np.array([2, 0, 1, 3, 1])

#h = [1, 1, 1]                  
#x = [1, 3, 1, 0, 2]
# y[n]=(1/3)*(x[n]+x[n-1]+x[n-2])

yOnPaper = [2, 2, 3, 4, 5, 4, 1]
print('yOnPaper = ', yOnPaper)
y = sp.convolve(h, x)
print('y = ', y)