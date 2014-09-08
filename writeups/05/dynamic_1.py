import math

def recursive_T(n):
    if n == 0 or n == 1:
        return 2
    SUM = 0
    for i in range(1, n):
        SUM+=recursive_T(i)*recursive_T(i-1)
    return SUM
def quadratic_T(n):
    if n == 0 or n == 1:
        return 2
    T = [0 for i in range(n+1)]
    T[0], T[1] = 2, 2
    for i in range(2, n+1):     #n+1 to include n
        SUM=0
        for j in range(1, n):   #range(1,n) to go only to n-1
            SUM+=T[j]*T[j-1]
        T[i] = SUM
    return T[n]
        
def linear_T(n):
    if n == 0 or n == 1:
        return 2
    T = [0 for i in range(n+1)]
    T[0], T[1], T[2] = 2, 2, 4
    for i in range(3, n+1):
        T[i] = T[i-1]*T[i-2] + T[i-1]
    return T[n]

if __name__ == '__main__':        
    for i in range(0, 25):
        recursive = recursive_T(i)
        quadratic = quadratic_T(i)
        linear = linear_T(i)
        
        if not (recursive == quadratic and quadratic == linear):
            print 'NOT EQUAL AT i=%i'%i
        else:
            print 'i=%i good' % i
        
