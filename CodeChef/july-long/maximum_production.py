for _ in range(int(input())):
    d , x , y , z = list(map(int , input().split()))
    strat_1 = 7*x
    strat_2 = d*y + (7 - d)*z
    print(max(strat_1 , strat_2))
