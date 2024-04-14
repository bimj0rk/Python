import numpy as np

d = np.array([6, 14, 18, 20, 21, 22, 23, 23.5, 24])
lambdaG = 26

for i in range(9):
    print(np.round(np.sqrt(1 + (1/np.sin(np.pi * d[i] / lambdaG))**2), decimals = 2))