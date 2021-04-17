class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        
        for row in range(n):
            for col in range(row, n):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
                
        for row in range(n):
            left = 0
            right = len(matrix[row]) - 1
            while left < right:
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                
                left += 1
                right -= 1
