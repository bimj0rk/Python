#%%
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

fs = 3000
ft = 200

fc = 1000

rp = 0.1
rs = 50

wp = np.array([fc + ft/2])/(fs/2)
ws = np.array([fc - ft/2])/(fs/2)

N, Wn = sp.cheb1ord(wp, ws, rp, rs)
b, a = sp.cheby1(N, rp, Wn, btype = 'low', output = 'ba')
Wn , h = sp.freqz(b, a, worN = 512, plot = None)
f = (fs/2) * Wn/np.pi

print(N)

plt.close('all')
plt.grid()
plt.plot(f, 10 * np.log10(abs(h)), linewidth = 3)
plt.show()
# %%
