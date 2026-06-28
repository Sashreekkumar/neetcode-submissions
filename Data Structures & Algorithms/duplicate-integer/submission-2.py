class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        flag = False
        for i in range(len(nums)):
                result = a.add(nums[i])
                if len(a) != (i+1):
                    flag = True
                    break
                else: flag = False
        if flag:
            return True
        else:
            return False
        
        
