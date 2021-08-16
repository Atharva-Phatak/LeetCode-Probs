import math 
for _ in range(int(input())):
    arr = list(map(int , input().split()))
    arr.sort()
    if (arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3]):
        print(0)
    elif ((arr[0] == arr[1] and arr[1] == arr[2]) or (arr[1] == arr[2] and arr[2] == arr[3])):
        print(1)
    else:
        print(2)
