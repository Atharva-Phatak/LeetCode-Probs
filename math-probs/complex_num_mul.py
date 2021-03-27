class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        [a1,b1,a2,b2] = map(int,(a+'+'+b).replace('i','').split('+'))
        return str(a1*a2-b1*b2)+'+'+str(a1*b2+a2*b1)+'i'
