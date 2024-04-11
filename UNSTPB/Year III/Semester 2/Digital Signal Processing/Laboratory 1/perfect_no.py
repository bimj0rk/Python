n = 1000
sumOfDivs = 0

for i in range(n):
    for x in range(1, i):
        if(x%2 == 0):
            sumOfDivs += x
    if(i == sumOfDivs):
        print("This number is perfet: ", i)
    