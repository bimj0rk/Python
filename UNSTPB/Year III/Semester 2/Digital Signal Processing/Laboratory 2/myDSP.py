import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def mySine(A, f, theta0, t):
    return(A * np.sin(2 * np.pi * f * t) + theta0)

def myCosine(A, f, theta0, t):
    return(A * np.cos(2 * np.pi * f * t) + theta0)

def myRamp(A, t1, t):
    return(A * (t >= t1))

def myBox(A, t1, t2, t):
    return(A * ((t >= t1) & (t < t2)))

def myWhiteNoise(A, t):
    n = np.random.rand(np.size(t))
    return(2 * A * (n - n.mean()))

def plotInTime(x, fs):
    t=np.arange(0, np.size(x, 0)/fs, 1/fs)
    plt.figure()
    plt.plot(t, x)
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    
def myDFT(x):
    N = np.size(x)
    X = np.zeros(N, dtype = complex)
    for k in range(N):
        for n in range(N):
            X[k] = X[k] + x[n] * np.exp(-2j * np.pi * k * n/N)
    return(X)


def play(x, fs):
    sd.play(x, fs)