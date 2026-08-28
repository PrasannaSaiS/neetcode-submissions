class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])
        low = 0
        high = height * width - 1

        while low <= high:
            mid = (low + high)//2
            if matrix[(mid//width)][mid%width] > target:
                high = mid - 1
            elif matrix[(mid//width)][mid%width] < target:
                low = mid + 1
            else: return True
        return False