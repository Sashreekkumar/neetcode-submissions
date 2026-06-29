class Solution:
    def getSum(self, a: int, b: int) -> int:
        aop = a & b
        oop = a | b
        return aop + oop