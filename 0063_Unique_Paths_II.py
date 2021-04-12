class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        return self.helper(obstacleGrid, 0, 0, memo)
    
    def helper(self, grid, i, j, memo):
        height = len(grid)
        width = len(grid[0])

        if (i, j) in memo:
            return memo[(i, j)]

        if grid[i][j] == 1:
            memo[(i, j)] = 0
            return 0
        else:
            if j == width - 1 and i == height - 1:
               memo[(i, j)] = 1
               return 1

            if i == height - 1:
                memo[(i, j)] = self.helper(grid, i, j + 1, memo)
                return memo[(i, j)]

            if j == width - 1:
                memo[(i, j)] = self.helper(grid, i + 1, j, memo)
                return memo[(i, j)]

            if i != height - 1  and j != width - 1:
                resA = self.helper(grid, i, j + 1, memo)
                resB = self.helper(grid, i + 1, j, memo)
                memo[(i, j)] = resA + resB
                return  memo[(i, j)]
