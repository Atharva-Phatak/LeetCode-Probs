import math
class Solution:
    
    def factor(self,n):
        if n == 1:
            return 1
        return n*self.factor(n-1)
    
    def getPermutation(self, n: int, k: int) -> str:
        z = [str(x) for x in range(n+1)]
        total = self.factor(n)
        print(total)
        ans =""
        while(z):
            total = total / n
            idx = math.ceil(k / total)
            ans += z.pop(idx - 1)
            k = k%total
            n = n - 1
        return ans
