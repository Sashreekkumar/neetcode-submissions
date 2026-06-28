class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        tables = {}
        tablet = {}
        for key in s:
            if key in tables:
                tables[key] += 1
            else:
                tables[key]= 1
        
        for key in t:
            if key in tablet:
                tablet[key] += 1
            else:
                tablet[key]= 1

        if tables == tablet:
            return True
        else:
            return False
        