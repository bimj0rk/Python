import numpy as np

x = np.array([[1, 0], [2, 0], [3, 0], [0, 1], [0, 2]])
t = np.array([[0], [0], [1], [0], [1]])

nExamples = np.size(x, 0)
x = np.concatenate((x, np.ones([nExamples, 1])), axis = 1)

nInputs = np.size(x, 1)
w = np.array([[1], [1], [2]])

def netOut(w, x):
    n = np.dot(x, w)
    y = n >= 0
    return y

eG = 1

while eG > 0:
    eG = 0
    y = netOut(w, x)
    e = t - y
    eG = sum(abs(e))
    dw = e * x
    dw = np.sum(dw, axis = 0)
    dw = np.reshape(dw, [nInputs, 1])
    w = w + dw
    
print(w)
print(netOut(w, x))