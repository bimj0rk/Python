import numpy as np
import time
import myDSP

N = 2048
x = np.random.rand(N)

t0 = time.time()
X1 = np.fft.fft(x)
t1 = np.finfo(float).eps

t0 = time.time()
X2 = myDSP.myDFT(x)
t2 = time.time() - t0

speedUp = t2/t1
print('speedUp = ', speedUp)