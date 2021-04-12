class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        return self.helper(grid, 0, 0, memo)
    
    def helper(self, grid, i, j, memo):

        height = len(grid)
        width = len(grid[0])

        if (i, j) in memo:
            return memo[(i, j)]

        if i == height - 1 and j == width - 1:
            memo[(i, j)] = grid[i][j]
            return grid[i][j]

        if i == height - 1:
            resA = self.helper(grid, i, j + 1, memo)
            memo[(i, j)] = grid[i][j] + resA
            return memo[(i, j)]

        if j == width - 1:
            resB = self.helper(grid, i + 1, j, memo)
            memo[(i, j)] = grid[i][j] + resB
            return memo[(i, j)]

        if i != height - 1  and j != width - 1:
            resA = self.helper(grid, i, j + 1, memo)
            resB = self.helper(grid, i + 1, j, memo)
            memo[(i, j)] = grid[i][j] + min(resA, resB)
            return memo[(i, j)]
