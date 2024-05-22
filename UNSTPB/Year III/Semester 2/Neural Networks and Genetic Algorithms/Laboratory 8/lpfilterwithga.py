#%%
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

def plotFreqResp(b):
    f,H=sp.freqz(b,1,nPoints, plot=None,fs=2)   
    H=abs(H)
    # H=H/H.max()
    plt.plot(f,H)
    plt.plot(f,idealH,'k')

def myPerf(b):
    _,H=sp.freqz(b,1,nPoints, plot=None,fs=2)
    H=abs(H)
    error=(idealH-H)**2
    perf=1/error.sum()
    return(perf)


plt.close('all')
nIndiv=50
nSel=10
r=.1 # +/- 10% for mutation
maxGen=400
N=15
perfFunct=np.zeros(nIndiv)

# LP at fc=fs/4
#_______
# |
# -----------
#0 fc=fs/4 fs/2

nPoints=64
Vmax=100
fc=0.5

idealH=np.linspace(0,1,nPoints)
idealH=idealH<=fc


pop=np.random.uniform(low = -Vmax, high = Vmax, size = (nIndiv,N))


for indexGen in range (maxGen):
    if np.mod(indexGen,10)==0:
        plt.figure()
        plotFreqResp(pop[0,:])

    for indiv in range(nIndiv):
        perfFunct[indiv]=myPerf(pop[indiv,:])
        # plt.plot(perfFunct,'o')
    order=np.argsort( perfFunct)[::-1] # sort in decreasing
        # plt.figure()
        # plt.plot(perfFunct[order],'o') # plot the performace ordered
    parents=pop[order[:nSel],:] # select the parents

        # print(parents[0]) # show the best individual
        ## print('=======================')
    pop=np.zeros([nIndiv,N])
    pop[:nSel,:]=parents
    perf=perfFunct[order[:nSel]]
    cs=np.cumsum(perf)
    cs=cs/cs[-1]
    for indexNewborn in range(nSel,nIndiv):
        select=np.random.rand()
        parentIndex=np.argmax((cs>select))
        pop[indexNewborn]=pop[parentIndex,:]*(1+2*r*(np.random.random(N)-.5))
# %%
