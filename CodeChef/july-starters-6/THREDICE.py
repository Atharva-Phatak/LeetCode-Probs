for _ in range(int(input())):
	x , y = list(map(int , input().split()))
	faces = [i for i in list(range(1,7)) if i > (x+y)]
	print(len(faces)/6)
