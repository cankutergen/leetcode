class Solution:
    def canCross(self, stones) -> bool:
        if stones is None or len(stones) == 0:
            return False

        memo = {}
        return self.dp(stones, 1, 1, stones[-1], memo)

    def dp(self, stones, position, k, target, memo):

        if position == target:
            return True

        if (position, k) in memo:
            return memo[(position, k)]

        if position in stones and k > 0:
            res = self.dp(stones, position + k - 1, k - 1, target, memo) or self.dp(stones, position + k, k, target, memo) or self.dp(stones, position + k + 1, k + 1, target, memo)
            memo[(position, k)] = res
            return res

        return False
