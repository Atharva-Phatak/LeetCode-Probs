# cook your dish here
import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int , input().split()))
    b = list(map(int , input().split()))

    a.sort()
    b.sort()
        
    list1 = []
    if b[0]-a[0] > 0:
        list1.append(b[0]-a[0])
    if b[0]-a[1] > 0:
        list1.append(b[0]-a[1])
        
    if len(list1) == 1:
        print(list1[0])
    else:

        sumA = sum(a)
        sumB = sum(b)

        list1.sort()

        for x in list1:
            if sumA-sumB+((n-1)*x) in a:
                print(x)
                break    
    
        
