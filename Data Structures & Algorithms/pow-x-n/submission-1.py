class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        if x == 1:
            return 1
        
        if n == 0:
            return 1
        
        prod = 1

        for i in range(abs(n)):
            prod *= x
        
        if n>0:
            return prod
        
        if n<0:
            return 1/prod