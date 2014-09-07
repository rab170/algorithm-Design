import math

def recursive_T(n):
    if n == 0 or n == 1:
        return 2
    SUM = 0
    for i in range(1, n):
        SUM+=recursive_T(i)*recursive_T(i-1)
    return SUM

def linear_T(n):
    if n == 0 or n == 1:
        return 2
    SUM = 0
    for i in range(1, n):
        SUM+=math.factorial(n)
    return SUM


    
for i in range(0, 10):
    print 'recursive_T(%i) = %i' %(i, recursive_T(i))
    
