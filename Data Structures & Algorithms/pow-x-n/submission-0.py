class Solution:
    def myPow(self, x: float, n: int) -> float:
        a = x
        
        if (n==0):
            x = 1
        
        elif (n>0):
            for _ in range(n-1):
                x*=a
        else:
            for _ in range(-(n+1)):
                x*=a
            
            x = 1/x
               
        return x