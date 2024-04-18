#%%
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

fs = 8000
fc = 2000
ft = 400

rp = 0.1
rs = 50

wp = np.array([fc - ft/2])/(fs / 2)
ws = np.array([fc + ft/2])/(fs / 2) #freq vectors, normalised

N, w = sp.cheb1ord(wp, ws, rp, rs)
b, a = sp.cheby1(N, rp, w) 
w, h = sp.freqz(b, a, worN = 512, plot = None)
f = (fs/2) * w/(np.pi)

print(N)

plt.close('all')
plt.plot(f, abs(h), linewidth = 3)
plt.plot([fc - ft/2], [1], 'or')
plt.plot([fc + ft/2], [0], 'or')
plt.xlabel('Frequency')
plt.ylabel('Gain')
plt.title('Frequency Response')
plt.grid()
# %%
