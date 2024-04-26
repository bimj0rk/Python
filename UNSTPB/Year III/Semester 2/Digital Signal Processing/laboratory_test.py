import scipy.signal as sp
import matplotlib.pyplot as plt
import numpy as np

fs = 22000
fc1 = 4000
fc2 = 6000
ft = 250

rp = 0.5
rs = 30

wp = np.array([fc1 - ft/2, fc2 + ft/2])/(fs/2)
ws = np.array([fc1 + ft/2, fc2 - ft/2])/(fs/2)

N, wN = sp.buttord(wp, ws, rp, rs)
b, a = sp.butter(N, wN, 'bandstop')
w, h = sp.freqz(b, a)
f = (fs/2) * (w/np.pi)
print('Filter order: ', N)

plt.plot(f, abs(h))
plt.xlabel('Frequency')
plt.ylabel('Gain')
plt.title('Frequency response')
plt.grid()
plt.show()
#fit to problem with a confidence of 70%