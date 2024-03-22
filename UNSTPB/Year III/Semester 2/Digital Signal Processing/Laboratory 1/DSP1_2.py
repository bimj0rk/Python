import numpy as np

R = 1
phi = 0
phi = float(phi)
N = 16
sortedArray = (np.empty([16, 2]))
for i in range(N):
    print("Phi = ", phi)
    cosComp = round(R * (np.cos(phi)), 4)
    print("cosComp = ", cosComp)
    sinComp = round(R * (np.sin(phi)), 4)
    print("sinComp = ", sinComp)
    
    currElement = np.array([[cosComp, sinComp]])
    np.insert(sortedArray, i, currElement, axis=0)
    
    phi += (np.pi)/2
    
    if(phi >= 2*(np.pi)):
        phi += (np.pi)/8
        
    N -= 1