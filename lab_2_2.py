import math

def a(k):
        if k == 1:
            return 1
        else:
            return (3 * b(k - 1) + 2 * a(k - 1))
        
def b(k):
        if k == 1:
            return 1
        else:
            return (a(k - 1) * a(k - 1) + b(k - 1))
        
def sum_expres(n):
    if n == 0:
        return 0
    k = 1
    suma = 0
    while k <= n:
        suma = suma + ((2**k) / (1 + a(k) + b(k)))
        k = k + 1
    return suma    

n = int(input('n = '))
print("Сума="+str(sum_expres(n)))
