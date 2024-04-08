#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

x = np.arange(-10, 10.1, 0.5)
b = np.sinc(x)

plt.close('all')
plt.figure()

a = np.array(1.)
w, H = sp.freqz(b, a, worN = 512, whole = False, plot = None)
f = w

# it may be also:
#f=w/(np.pi)
#f=(w/(np.pi))*(fs/2)

plt.subplot(1, 2, 1)
plt.plot(b, '.-')
plt.title('Filter Coefficients')
plt.grid(True)


plt.subplot(1, 2, 2)
plt.plot(f, abs(H), '.-')
plt.title('Transfer function')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid(True)

# %%
