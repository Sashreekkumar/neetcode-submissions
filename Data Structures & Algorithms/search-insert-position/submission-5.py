class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        flag = False
        while l <= r:
            m = l + ((r-l)//2)
            if nums[m]==target:
                flag = True
                break
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        if flag:
            return m
        else:
            if target > nums[m]:
                return m + 1
            else:
                return m 
        