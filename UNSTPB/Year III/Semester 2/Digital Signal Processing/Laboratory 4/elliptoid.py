#%%
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

fs = 15000
fc1 = 3000
fc2 = 6000
ft = 150

rp = 2 #to search about
rs = 20 #to search about

wp = np.array([fc1 + ft/2, fc2 - ft/2])/(fs / 2)
ws = np.array([fc1 - ft/2, fc2 + ft/2])/(fs / 2)

N, w = sp.ellipord(wp, ws, rp, rs)
b, a = sp.ellip(N, rp, rs, w, btype = 'bandstop')
w, h = sp.freqz(b, a, worN = 512, plot = None)
f = (fs/2) * w/np.pi


print(N)

plt.close('all')
plt.plot(f, 20*np.log10(abs(h)))
plt.plot([fc1 - ft/2, fc2 - ft/2], [1], 'ro')
plt.plot([fc1 + ft/2, fc2 + ft/2], [0], 'ro')
plt.xlabel("Freq")
plt.ylabel("gain")
# %%
