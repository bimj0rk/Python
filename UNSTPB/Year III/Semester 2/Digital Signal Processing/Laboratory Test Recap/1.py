#%%
#fc - 400-1200
#ft - 150
#rp-rs : 0.2-50
#highpass
#cheby ii

import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

fs = 3000
ft = 150
fc1 = 400
fc2 = 1200
rp = 0.2
rs = 50

wp = np.array([fc1 + ft/2, fc2 - ft/2])/(fs/2)
ws = np.array([fc1 - ft/2, fc2 - ft/2])/(fs/2)

N, Wn = sp.cheb2ord(wp, ws, rp, rs)
b, a = sp.cheby2(N, rs, Wn, btype = 'high', output = 'ba')
w, h = sp.freqz(b, a, worN = 512, plot = None)
f = (fs/2) * w/np.pi

plt.close('all')
plt.grid()
plt.plot(f, 20 * np.log10(abs(h)), linewidth = 3)
plt.show()
# %%
