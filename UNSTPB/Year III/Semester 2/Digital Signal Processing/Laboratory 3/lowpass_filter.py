#%%

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.1, 0.5)
h = np.sinc(x)


plt.close('all')

plt.subplot(2, 2, 1)
plt.plot(h, '.-')
plt.title('Cardinal Sinus in time')
plt.grid(True)
#This is under sampled

H = np.fft.fft(h)
plt.subplot(2, 2, 2)
plt.plot(abs(H), '.-')
plt.title('Fourier Transform')
plt.grid(True)

plt.subplot(2, 2, 4)
N = int(len(H)/2)
plt.plot(abs(H)[:N], '.-')
plt.title('Halfband for the Fourier Transform')
plt.grid(True)
#This shows that this is a low-pass filter

#no ripple in band to be a good audio filter
#information can be transmitted through phase, not only through amplitude