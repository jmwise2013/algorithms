#Here is a recursive function that returns the integer sum of the numbers between 0 and input n.
#rSigma(0) = 0, rSigma(1) = 1, rSigma(2) = 3, etc.
#Python's "trunc" function will truncate a float, such as 6.5, down to its integer, in this case 6.


import math

def rSigma(n):
    if n<= 0:
        return 0
    else:
        return rSigma(math.trunc(n)-1) + math.trunc(n)

print(rSigma(0))
print(rSigma(1))
print(rSigma(2))
print(rSigma(5))
print(rSigma(6.5))