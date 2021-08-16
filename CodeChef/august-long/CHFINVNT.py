from math import floor
for _ in range(int(input())):
    n,p,k = list(map(int , input().split()))
    ans = 0
    
    x=p%k - 1 
    y=((n-1)//k)*k
    y=n-1-y
    if (x>y):
        ans+=(y+1)*((n-1)//k + 1)+ (x-y)*((n-1)//k)
    else:
        ans+=((n-1)//k + 1)*(x+1)
    for i in range(x+1,n,k):
        ans+=1
        if(i==p):
            print(ans)
            break
