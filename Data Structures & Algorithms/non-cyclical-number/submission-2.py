class Solution:
    def isHappy(self, n: int) -> bool:

        def sumofsquare(n: int) -> int:
            sos = 0
            while n:
                sos += (n%10)**2
                n //= 10
            return sos

        freq = set()

        while n not in freq:
            freq.add(n)
            n = sumofsquare(n)

            if n == 1:
                return True
            
        return False