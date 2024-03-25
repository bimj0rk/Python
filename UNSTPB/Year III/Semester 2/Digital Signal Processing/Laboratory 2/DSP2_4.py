import numpy as np
import myDSP

x = np.array([0, 1, 2, 3])
 
X1 = myDSP.myDFT(x)
print(X1)

X2 = np.fft.fft(x)
print(X2) 