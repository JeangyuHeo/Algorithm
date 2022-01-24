class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = (len(matrix[0]) * len(matrix)) - 1
        
        while start <= end:
            avg = (start + end) // 2
            
            if matrix[avg // len(matrix[0])][avg % len(matrix[0])] < target:
                start = avg + 1
            elif matrix[avg // len(matrix[0])][avg % len(matrix[0])] > target:
                end = avg - 1
            else:
                return True
        return False