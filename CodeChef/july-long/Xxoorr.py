import math
def decimalToBinary(arr):
    b = [bin(n).replace("0b", "") for n in arr] 
    m = len(max(b , key = len))
    b = [x.rjust(m , '0') for x in b]
    return b
        

def fill_z(n):
    
    z = [0]*32
    idxs = []
    bin_str = decimalToBinary(n)
    for s in bin_str:
        idxs.extend([i for i in range(len(s)) if s[i] == '1'])
    for i in idxs:
        z[i] += 1
    return z

for _ in range(int(input())):
    _ , k = list(map(int , input().split()))
    n = list(map(int, input().split()))
    z = fill_z(n)
    ans = 0
    for i in z:
        ans += math.ceil(i / k)
    print(ans)
