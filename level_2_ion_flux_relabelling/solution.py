def power_2(h):
    result = 1
    for i in range(h):
        result*=2
    return result

def solve(h, num):
    pow2h = power_2(h)
    if num % (pow2h-1) == 0: return -1
    if h==2: return 3
    pow2h_minus_1 = int(pow2h/2)-1
    rem = num%pow2h_minus_1
    solution = solve(h-1, rem)
    if solution==-1: return pow2h-1
    return solution + int(num/pow2h_minus_1)*pow2h_minus_1

def solution(h, q):
    # Your code here
    p = []
    for elem in q:
        p.append(solve(h, elem))
        
    return p