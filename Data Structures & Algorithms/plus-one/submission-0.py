class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int("".join(map(str, digits)))
        result += 1
        num = [int(digit) for digit in str(result)]
        return num
        