class Solution:
    def isPalindrome(self, s: str) -> bool:
        def cleantext(s: str) -> str:
            punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            s = s.replace(" ", "")
            s = s.lower()
            s = s.translate(str.maketrans("", "", punctuation))

            return s
        
        s = cleantext(s)
        l = 0 
        r = len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True



        

        