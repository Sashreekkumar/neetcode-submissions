class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        l1 = len(word1)
        l2 = len(word2)
        res = ""
        for i in range(min(l1, l2)):
            res = res + word1[p1] + word2[p2]
            p1 += 1
            p2 += 1
        
        if l1 == l2:
            return res
        elif l1 > l2:
            res = res + word1[p1:l1]
            return res
        else:
            res = res + word2[p2:l2]
            return res
        