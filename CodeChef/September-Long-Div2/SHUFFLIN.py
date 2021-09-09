for _ in range(int(input())):
    n = int(input())
    arr = list(map(int , input().split()))
    even, odd = 0,0
    for ele in arr:
        if ele % 2 == 1:
            odd += 1
        else:
            even += 1
    
    s = min(odd , n//2) + min(even , (n+1)//2)
    print(s)
