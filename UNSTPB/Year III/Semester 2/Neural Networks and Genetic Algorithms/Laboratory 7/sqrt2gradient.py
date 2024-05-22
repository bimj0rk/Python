import numpy as np

def myFunct(x):
    return((x**2-2)**2)

def myFunctGrad(x):
    return(4*x**3-4*x)

alpha=0.0001

x=10*np.random.rand(1)

myEps=10**-6

myError=1

index=1
while myError>myEps:
    dx=-alpha*myFunctGrad(x)
    x=x+dx
    myError=abs(myFunct(x)) 
    print(myError)
    index=index+1

print('========')
print(x)