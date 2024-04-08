# FIR filter design
#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp


w = [.2, .5]
filterOrder = [9, 27, 81, 243]
a = np.array(1.)

plt.close('all')

for N in filterOrder:
    b = sp.firwin(N, w)
    
    f, H = sp.freqz(b, a, worN = 512, whole = False, plot = None)
    f = f/(np.pi) #normalized frequency, we can use this type of filter for sampling
    
    F = plt.figure()
    F.suptitle('FIR filter of order ' + str(N))
    
    plt.subplot(1, 2, 1)
    plt.plot(b, '.-')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(f, abs(H))
    plt.grid(True)
    

# %%
