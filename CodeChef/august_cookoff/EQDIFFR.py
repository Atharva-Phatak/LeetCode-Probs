from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int , input().split()))
    if n<3:
        print('0')
    else:
        result = n - 2
        counts = Counter(arr)
        num, count = counts.most_common(1)[0]
        result = min(result, n - count)
        print(result)
