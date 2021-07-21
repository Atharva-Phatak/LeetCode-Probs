# cook your dish here
import sys, io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

class FenwickTree:
    
    def __init__(self, n):
        self.bit = [0]*(n+1)
    
    def update(self, i,n,val):
        i += 1
        while i<=n:
            self.bit[i] += val
            i += (i&(-i))
    
    def get_sum(self, idx):
        idx += 1
        s = 0
        while idx>0:
            s += self.bit[idx]
            idx = idx - (idx&(-idx))
        return s
        
def update(ft, l ,r , n , val):
    ft.update(l,n,val)
    ft.update(r+1,n, -val)

n,q = list(map(int , input().decode().split()))
arr = list(map(int , input().decode().split()))
ft1, ft2, ft3 = FenwickTree(n) , FenwickTree(n) , FenwickTree(n)

for _ in range(q):
    query = list(map(int , input().decode().split()))
    if query[0] == 1:
        l,r,x = query[1] -1 , query[2] - 1, query[3]
        val = x-l
        update(ft1, l,r,n,1)
        update(ft2, l , r,n,val**2),
        update(ft3, l,r, n,2*val)
    else:
        idx = query[1] - 1
        ans = arr[idx] + idx**2*(ft1.get_sum(idx)) + ft2.get_sum(idx) + idx*ft3.get_sum(idx)
        sys.stdout.write(f"{str(ans)}")
        sys.stdout.write("\n")
