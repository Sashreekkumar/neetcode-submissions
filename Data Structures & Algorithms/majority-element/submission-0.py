class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        freq = []
        for i in nums:
            hash_map[i] = hash_map.get(i,0)+1
        for i in hash_map.values():
            freq.append(i)
        freq.sort()
        len_freq = len(freq)
        high_freq = freq[len_freq - 1]
        
        for key, value in hash_map.items():
            if value == high_freq:
                return key
                break



        