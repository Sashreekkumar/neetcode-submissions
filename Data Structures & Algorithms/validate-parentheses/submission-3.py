class Solution:
    def isValid(self, s: str) -> bool:
        directory = {")":"(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i not in directory:
                stack.append(i)
            else:
                if stack and stack[-1] == directory[i]:
                    stack.pop()
                else:
                    stack.append(i)
        return True if not stack else False