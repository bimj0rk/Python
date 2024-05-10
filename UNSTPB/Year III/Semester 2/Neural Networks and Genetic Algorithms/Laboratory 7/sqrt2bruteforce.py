#brute force

import numpy as np

def myFunct(x):
    return(x**2-2)

def myError(x):
    return (abs(myFunct(x)))

step=10**(-4)
error=100
a=0
b=3
grid=np.arange(a,b,step)

for x in grid:
    e=myError(x)
    if e<error:
        mySol=x
        error=e
        print(e)

print('==============')
print(mySol)