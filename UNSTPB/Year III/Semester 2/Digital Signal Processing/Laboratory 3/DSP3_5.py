#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

b = np.array([0,  2, -9, 19, 75, 19, -9,  2,  0])


plt.close('all')

a = np.array(1.) #sigma function
w,H = sp.freqz(b, a, worN = 512, whole = False, plot = None)
f = w/(np.pi)

plt.plot(f, abs(H))
plt.title('Transfer function')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid(True)

# %%
