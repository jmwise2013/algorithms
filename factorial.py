# Here is a simple function that calculates the factorial of an input "n" in Python.
# Note: the "trunc" function will take a float like 6.5 and truncate it to an integer.
# Note: this is also a "recursive" function that calls itself multiple times instead of utilizing a loop.

import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return math.trunc(n) * factorial(math.trunc(n)-1)

print(factorial(0))
print(factorial(3))
print(factorial(6.5))

