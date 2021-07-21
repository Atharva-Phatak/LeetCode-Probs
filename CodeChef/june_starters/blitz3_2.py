for _ in range(int(input())):
    n , a , b = list(map(int , input().split()))
    print(int(2*(180 + n) - (a+b)))
