
def solution(l):
    if l==[]: return 0
    count = 0
    first_div = {}
    for i in range(1, len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                first_div[i] = (1 if i not in first_div else first_div[i]+1)
                count += (0 if j not in first_div else first_div[j])

    return count
