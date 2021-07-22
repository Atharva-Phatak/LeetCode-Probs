for _ in range(int(input())):
	n,k = list(map(int , input().split()))
	A = list(map(int , input().split()))
	A.sort(reverse = True)
	i = 0
	chef, twin = 0,0
	while(k > 0):
		chef += A[i]
		twin += A[i+1]
		i += 2
		k = k -1

	twin += A[i]
	print(max(twin , chef))