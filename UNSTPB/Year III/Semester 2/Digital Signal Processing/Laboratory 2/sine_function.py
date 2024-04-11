import numpy as np
import matplotlib.pyplot as plt
import myDSP
import sounddevice as sd

def mySine(A, f, ph0, t):
    return(A * np.sin(2 * np.pi * f * t + ph0))

t0 = 0 
t1 = 1 
fs = 100 

t = np.arange(t0, t1+1/fs, 1/fs)

A = 2
f = 3
ph0 = 0

y = myDSP.mySine(A, f, ph0, t)

plt.close('all')
plt.plot(t, y)
plt.xlabel('time(s)')
plt.grid() 