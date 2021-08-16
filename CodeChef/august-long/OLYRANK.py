for _ in range(int(input())):
    arr = list(map(int, input().split()))
    c1 = sum(arr[:3])
    c2 = sum(arr[3:])
    if c1>c2:
        print(1)
    else:
        print(2)
