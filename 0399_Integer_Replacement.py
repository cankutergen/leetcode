class Solution:
    def integerReplacement(self, n: int) -> int:
        return self.dp(n, 0)
        
    def dp(self, n, count):
        if n == 1:
            return count

        if n % 2 == 1:
            return min(self.dp(n - 1, count + 1), self.dp(n + 1, count + 1))
        else:
            return self.dp(int(n / 2), count + 1)
