upper_bound = 10**5
aux_array = [0]*(upper_bound + 1)
for c in range(1, upper_bound//2 + 1):
    for b in range(c , upper_bound+1, c):
        if b%c == 0:
            for a in range(c , upper_bound+1, b):
                if a%b == c:
                    if a>b:
                        aux_array[a] += 1
                    else:
                        aux_array[b] += 1


for _ in range(int(input())):
    n = int(input())
    print(sum(aux_array[:n+1]))
