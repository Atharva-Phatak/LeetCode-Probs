import math
for _ in range(int(input())):
    n,a = list(map(int , input().split()))
    ans = int(math.sqrt(n))
    print(ans*a)
