class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i=="+":
                res = stack[-1] + stack[-2]
                stack.append(res) 

            elif i=="C":
                stack.pop()

            elif i=="D":
                res = stack[-1] * 2
                stack.append(res)
            
            else:
                stack.append(int(i))
        
        s = 0
        for i in stack:
            s+=i
        return s

        