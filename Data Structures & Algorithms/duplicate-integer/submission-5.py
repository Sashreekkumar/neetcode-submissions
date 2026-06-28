class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsset = set()
        for i in range(len(nums)):
            numsset.add(nums[i])       
            if len(numsset) != (i+1):
                return True
        
        return False