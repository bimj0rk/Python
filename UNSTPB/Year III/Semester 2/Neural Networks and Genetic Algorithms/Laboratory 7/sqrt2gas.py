import numpy as np
import matplotlib.pyplot as plt

def myFunct(x):
    return(x**2-2)

def myPerf(x):
    return (1/abs(myFunct(x)))

def generate(a,b):  
    return(a+(b-a)*np.random.rand(1))

nIndiv=100
a=0
b=3
step=10**(-4)
N=(b-a)/step
nGenerations=int(N/nIndiv)
nGenerations=int(nGenerations/10)

pop=a+(b-a)*np.random.rand(nIndiv)

nSel=10
r=.01 # +/- 10% for mutation

for indexGen in range(nGenerations): #nGenerations):
    perfFunct=myPerf(pop) # compute performance function
    order=np.argsort( perfFunct)[::-1] # sort in decreasing
    # plt.plot(perfFunct[order]) # plot the performace ordered
    parents=pop[order[:nSel]] # select the parents
    print(parents[0]) # show the best individual
    # print('=======================')
    pop=np.zeros(nIndiv)
    pop[:nSel]=parents
    perf=myPerf(parents)
    # print(perf)
    cs=np.cumsum(perf)
    cs=cs/cs[-1]
    for indexNewborn in range(nSel,nIndiv):
        select=np.random.rand()
        parentIndex=np.argmax((cs>select))
        pop[indexNewborn]=pop[parentIndex]*(1+2*r*(np.random.random()-.5))
print('==================')
print(2**.5)