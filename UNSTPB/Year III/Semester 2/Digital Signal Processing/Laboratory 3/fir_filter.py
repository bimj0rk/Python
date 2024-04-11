#%%
# FIR filter design
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

w = .75
N = 100


b = sp.firwin(N, w)
a = np.array(1.)

w,H = sp.freqz(b, a, worN = 512, whole = False, plot = None)
f = w/(np.pi)

#plt.close('all')
plt.figure()

plt.subplot(1, 2, 1)
plt.plot(b, '.-')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(f, abs(H))
plt.grid(True)

print(np.round(100 * b))
# %%
