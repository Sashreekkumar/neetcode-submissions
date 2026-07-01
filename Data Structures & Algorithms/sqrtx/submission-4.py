class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x==0:
            return 0
        if x==1:
            return 1
    
        l = 0
        r = x//2

        res = 0

        while l <= r:
            m = l + ((r - l)//2)
            if m*m == x:
                return m
            elif m*m > x:
                r = m - 1
            else:
                l = m + 1
                res = m

        return res
        