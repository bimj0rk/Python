import numpy as np
import matplotlib.pyplot as plt
import myDSP
import sounddevice as sd

t0 = 0 
t1 = 1 
fs = 22050

t = np.arange(t0, t1+1/fs, 1/fs)

A = 1
f = 440

y = myDSP.mySine(A, f, 0, t)

plt.close('all')
plt.plot(t, y)
plt.axis([0,5 * 10 ** -3, -1, 1])
plt.xlabel('time(s)')
plt.grid() 
sd.play(y, fs)
print('ok')
# %%
