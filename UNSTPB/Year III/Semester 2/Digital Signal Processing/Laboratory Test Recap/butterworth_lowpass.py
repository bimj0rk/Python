#%%
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

fs = 13000
ft = 250

fc = 4500

rp = 4
rs = 6

wp = (fc + ft/2)/(fs/2)
ws = (fc - ft/2)/(fs/2)

N, w = sp.buttord(wp, ws, rp, rs)
b, a = sp.butter(N, w, btype = 'low', output = 'ba')
w, h = sp.freqz(b, a, worN = 512, plot = None)
f = (fs/2) * w/np.pi

print(N)

plt.close('all')
plt.grid()
plt.plot(f, 20 * np.log10(abs(h)), linewidth = 2)
plt.show()

# %%
