import numpy as np
import scipy.signal as dsp
import matplotlib.pyplot as plt

N = 64

x = np.random.rand(N, 1)
y = np.random.rand(N, 1)

plt.subplot(3, 2, 1)
plt.plot(x, 'b.-')
plt.subplot(3, 2, 3)
plt.plot(y, 'r.-')

conv1 = dsp.convolve(x, y)
plt.subplot(3, 2, 5)
plt.plot(conv1, 'g.-')

X = abs(np.fft.fft(x, axis = 0))
Y = abs(np.fft.fft(y, axis = 0))

plt.subplot(3, 2, 2)
plt.plot(X, 'b.-')

plt.subplot(3, 2, 4)
plt.plot(Y, 'r.-')