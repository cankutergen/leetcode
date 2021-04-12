class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.num_ways(n, [1, 2], memo)
        
        
    def num_ways(self, n, x, memo):
        if n == 0:
            return 1
        
        if n in memo:
            return memo[n]

        total = 0
        for i in x:
            if n - i >= 0:
                total += self.num_ways(n - i, x, memo)
        
        memo[n] = total
        return total
