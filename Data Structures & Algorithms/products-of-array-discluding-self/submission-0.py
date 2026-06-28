class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        zero_index = []
        prod = 1
        for index, value in enumerate(nums):
            if value == 0:
                zero_count += 1
                zero_index.append(index)

        if zero_count > 1:
            return [0]*len(nums)
        
        if zero_count == 1:
            op = [0] * len(nums)
            del nums[zero_index[0]]
            for i in nums:
                prod *= i
            op[zero_index[0]] = prod
            return op
        
        for i in nums:
            prod *= i
        

        op = [prod] * len(nums)

        for i in range(len(nums)):
            op[i] //= nums[i]
        return op



            
        