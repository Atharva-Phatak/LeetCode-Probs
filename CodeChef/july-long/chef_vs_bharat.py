def get_chefora(n):
    if len(str(n)) == 1:
        return n
    else:
        temp = str(n)
        return int(temp + (temp[:-1])[::-1])


p = (10**9+7)
n = 10**5+1
chefora_array = [0]*(n)
chefora_array[0] = 0
for i in range(1,n):
    chefora_array[i] = get_chefora(i)
        
prefix_sum = [0]*(n)
prefix_sum[0] = 0
prefix_sum[1] = chefora_array[1]
for i in range(2, n):
    prefix_sum[i] = prefix_sum[i-1] + chefora_array[i]
    
for _ in range(int(input())):
    l,r = list(map(int,input().split()))
    s = prefix_sum[r] - prefix_sum[l]
    ans = pow(chefora_array[l] , s, p)
    print(ans)
