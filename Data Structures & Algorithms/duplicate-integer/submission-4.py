class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i, num in enumerate(nums):
            seen.add(num)

            if len(seen) != i + 1:
                return True

        return False