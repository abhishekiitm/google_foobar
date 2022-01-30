def XOR(start, length):
    if length <= 4:
        checksum = 0
        for i in range(length):
            checksum = checksum^(start+i)
        return checksum
    if start & 1 == 0:
        l_checksum = 0
    else:
        l_checksum = start
    r_start = start + 4*int((length-1)/4) + int(start&1)
    for j in range(r_start, start+length):
        l_checksum = l_checksum^j
    return l_checksum

def solution(start, length):
    # Your code here
    checksum = 0
    for i in range(length):
        line_start = start+length*i
        checksum = checksum ^ XOR(line_start, length-i)
    return checksum
