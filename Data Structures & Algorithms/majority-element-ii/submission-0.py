class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        op = []
        for key, value in freq.items():
            if value > len(nums)/3:
                op.append(key)
        
        return op

                

        
        