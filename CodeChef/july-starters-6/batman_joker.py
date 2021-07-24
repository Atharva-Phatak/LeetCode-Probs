
for _ in range(int(input())):
	n , m, l = list(map(int , input().split()))
	color_d = {}
	for i in range(m):
		op = list(map(int , input().split()))
		for color in op:
			color_d[color] = i

	strip = list(map(int , input().split()))
	temp = hash_color[strip[0]]
	sol = 1
	for i in range(1, len(strip)):
		if hash_color[L[i]] != temp:
			sol += 1
			temp = hash_color[L[i]]
	print(temp)