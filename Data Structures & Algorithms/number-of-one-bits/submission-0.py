class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(n.bit_length()):
            if n & (1<<i) != 0:
                res+=1
        
        return res 