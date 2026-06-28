class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        op = []
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for i in range(k):
            op.append(max(freq, key = freq.get))
            del freq[op[i]]
        
        return op

        
        

        