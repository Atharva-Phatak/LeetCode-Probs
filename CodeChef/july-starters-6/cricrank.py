for _ in range(int(input())):
	r1,w1,c1 = list(map(int , input().split()))
	r2,w2,c2 = list(map(int , input().split()))

	score_a , score_b = 0,0
	if r1 > r2 :
		score_a += 1
	elif r2 > r1 :
		score_b += 1
	if w1 > w2: 
		score_a += 1
	elif w2 > w1:
		score_b += 1
	if c1 > c2:
		score_a += 1
	elif c2 > c1:
		score_b += 1

	if score_a > score_b:
		print("A")
	else:
		print("B")