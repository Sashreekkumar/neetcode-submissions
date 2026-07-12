
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def get_high_bits(number):
            indices = []
            total_bits = number.bit_length() 
            for i in range(total_bits):
                if (number & (1 << i)) != 0:
                    indices.append(i)
            
            return indices
        
        count = pow(2, len(nums))
        subsets = [[]]
        for i in range(count-1):
            bits = get_high_bits(i+1)
            subset = []
            for j in bits:
                subset.append(nums[j])
            subsets.append(subset)
        
        return subsets
