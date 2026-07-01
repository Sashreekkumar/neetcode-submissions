class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        m = nums[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i] == m:
                count += 1
            else:
                count -= 1
            if count < 0:
                m = nums[i]
            
        return m
            
            

        