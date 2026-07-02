class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def str2int(num: str) -> int:
            nums = ["0","1","2","3","4","5","6","7","8","9"]
            n = []
            for i in num:
                n.insert(0, nums.index(i))
            return n

        num1 = str2int(num1)
        num2 = str2int(num2)
        n1 = 0
        n2 = 0

        for index, value in enumerate(num1):
            n1 += value * (10**index)
        
        for index, value in enumerate(num2):
            n2 += value * (10**index)
        
        prod = n1 * n2
        n = 0
        op = []
        while prod:
            n  = prod % 10
            prod //= 10
            op.insert(0,n)

        return "".join(map(str, op))


        




        


            


                
        


        


        