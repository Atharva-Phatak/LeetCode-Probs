for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    arr = list(map(int , input().split()))
    arr.sort()
    for i in range(k):
        if arr[i] < 0:
            arr[i] = arr[i]*(-1)
    
    s = 0
    for ele in arr:
        if ele > 0:
            s += ele
    
    print(s)
