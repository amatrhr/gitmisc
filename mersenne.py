import math
from collections import Counter
def eucl_alg(a, b):
    if min(a,b) == 1:
        return(1)
    if a == b:
        return(a)
    elif (b - a > 0):
        return(eucl_alg(a, b-a))
    else:
        # have ruled out equality and b > a
        # so must have a > b
        return(eucl_alg(a-b, b))


eval_bin = lambda x: not('0' in str(bin(x))[1:])

candidates = [x for x in range(0,200000) if eval_bin(x)]

def aritos(x):
    ub = x//2
    check=[j for j in range(ub+1) if math.gcd(x,j)==1]

    if len(check) == x//2:
        return(True)
    else:
        return(False)
    
checks = {x:aritos(x) for x in candidates}
print(checks)
print(Counter(checks.values()))
