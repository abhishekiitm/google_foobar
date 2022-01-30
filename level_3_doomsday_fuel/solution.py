import numpy as np
from functools import reduce
from fractions import Fraction

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def common_integer(numbers):
    fractions = [Fraction(n).limit_denominator() for n in numbers]
    multiple  = reduce(lcm, [f.denominator for f in fractions])
    ints      = [int(f * multiple) for f in fractions]
    divisor   = reduce(gcd, ints)
    return [int(n / divisor) for n in ints]

def solution(m):
    absorbing, transient = [], []
    for i, row in enumerate(m):
        if not any(row):
            absorbing.append(i)
        else:
            transient.append(i)
            row_sum = float(sum(row))
            for j in range(len(row)):
                m[i][j]=m[i][j]/row_sum

    if 0 in absorbing:
        ret = [0]*(len(m)+1)
        ret[0], ret[-1] = 1
        return ret

    M = np.array(m)[transient]
    Q = M[:,transient]
    R = M[:,absorbing]
    N = np.linalg.inv(np.subtract(np.identity(len(transient)), Q))
    NR = np.matmul(N,R)[0]
    result = common_integer(list(NR))
    result = [int(round(r)) for r in result]

    result.append(sum(result))

    return result