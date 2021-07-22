for _ in range(int(input())):
	a,b,c,d,k = list(map(int , input().split()))
	dist = abs(a-c) + abs(b-d)
	if (k >= dist and k%2 == dist%2):
		print("Yes")
	else:
		print("No")