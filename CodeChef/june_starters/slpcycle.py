def count_zeros(s):
    return [len(ele) for ele in s.split("1") if len(ele) != 0]

for _ in range(int(input())):
    l,h = list(map(int , input().split()))
    s = input()
    z = count_zeros(s)
    for ele in z:
        if ele > h/2:
            h = 2*(h-ele)
    if h<=0:
        print("Yes")
    else:
        print("No")
