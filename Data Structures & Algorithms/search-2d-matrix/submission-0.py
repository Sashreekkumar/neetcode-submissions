class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                left = 0
                right = cols - 1

                while left <= right:
                    m = (left + right) // 2

                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        left = m + 1
                    else:
                        right = m - 1

                return False

        return False