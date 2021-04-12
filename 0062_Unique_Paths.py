class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        return self.helper(m, n, 0, 0, memo)
        
    def helper(self, m, n, i, j, memo):
        height = m
        width = n

        if (i, j) in memo:
            return memo[(i, j)]

        if i == height - 1 and j == width - 1:
            memo[(i, j)] = 1
            return 1

        if j == width - 1 or i == height - 1:
            memo[(i, j)] = 1
            return 1

        if i != height - 1  and j != width - 1:
            resA = self.helper(m, n, i, j + 1, memo)
            resB = self.helper(m, n, i + 1, j, memo)
            memo[(i, j)] = resA + resB
            return  memo[(i, j)]
