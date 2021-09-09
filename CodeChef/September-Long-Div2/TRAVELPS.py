from collections import Counter
for _ in range(int(input())):
    n,a,b = list(map(int , input().split()))
    s = input()
    ct = Counter(s)
    print(ct['0']*a + ct['1']*b)
