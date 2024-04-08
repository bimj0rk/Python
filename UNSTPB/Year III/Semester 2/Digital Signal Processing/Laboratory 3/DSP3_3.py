import scipy.signal as sp
import numpy as np

x = np.array([1, 0, 2, 1])

b = np.array([1, 2, 3, 0, 2])
b = b.astype(float)

zConv = sp.convolve(x, b)
print('conv = ', zConv)
zConv = sp.convolve(b, x)
print('conv = ', zConv)

a = np.array(1.)

zFilter = sp.lfilter(b, a, x)
print('filtering = ', zFilter)

x = np.array([1., 0., 0., 0, 0, 0, 0, 0, 0])
zFilter = sp.lfilter(b, a, x)
print('impulse response = ', zFilter)

#               b =     1,2,3,0,2
#       x=                              0 0 0 1 0 0  
#CONVOLUTION