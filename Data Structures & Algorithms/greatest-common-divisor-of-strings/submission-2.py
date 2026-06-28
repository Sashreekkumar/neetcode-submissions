class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        factors = []
        for i in range(-(-l1//2)):
            mult = l1//(i+1)
            if (str2[:i+1]*mult == str1):
                factors.append(str2[:i+1])
        
        if not factors:
            return ""
        return factors[len(factors)-1]

        

        