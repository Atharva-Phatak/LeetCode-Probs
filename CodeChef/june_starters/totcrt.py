import sys, io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
for _ in range(int(input().decode())):
    n = int(input().decode())
    d = {}
    for _ in range(n*3):
        prob , crrct = input().decode().split()
        if prob not in d:
            d[prob] = int(crrct)
        else: 
            d[prob] += int(crrct)
    
    
    for ele in sorted(list(d.values())):
        sys.stdout.write(f"{str(ele)} ")
    sys.stdout.write("\n")
