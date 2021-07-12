from math import gcd , inf
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int , input().split()))
    
    if len(arr) == 1:
        print(1)
        continue
    
    prefix = [0]*n
    suffix = [0]*n
    z = [0]*n
    
    prefix[0] = arr[0]
    suffix[n-1] = arr[n-1]
    
    for i in range(1,n):
        prefix[i] = gcd(prefix[i-1] , arr[i])
    
    for i in range(n-2,-1,-1):
        suffix[i] = gcd(suffix[i+1] , arr[i])
    
    z[0] = suffix[1]
    z[n-1] = prefix[n-2]
    
    for i in range(1 , n-1):
        z[i] = gcd(prefix[i-1] , suffix[i+1])
    
    s = sum(arr)
    
    ans = inf
    for i in range(n):
        op = int((s - arr[i] + z[i]) / z[i])
        ans = min(op , ans)
    print(ans)
