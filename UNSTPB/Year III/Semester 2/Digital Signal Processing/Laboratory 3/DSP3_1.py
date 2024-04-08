#%%
import numpy as np
import matplotlib.pyplot as plt


f = np.arange(0, 1, 0.01)
h = (f>0.6) & (f<0.7)

H = np.abs(np.fft.fft(h))

plt.close('all')
plt.subplot(2, 2, 1)
plt.plot(f, h)
plt.title('box in time')

plt.subplot(2, 2, 2)
plt.plot(H)
plt.title('Modulus of DFT - symmetrical')

plt.subplot(2, 2, 4)
N = int(len(H)/2)
plt.plot(np.arange(-N, N),np.concatenate((H[N:], H[0:N])))
plt.title('Modulus of DFT - centered in origin')

#NO PHASE
# %%
