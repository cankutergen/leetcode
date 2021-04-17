class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        memo = {}
        return self.dfs(nums, memo, 0, -sys.maxsize)

    def dfs(self, nums, memo, i, pre):
        if i == len(nums):
            return 0
        if (i, pre) in memo:
            return memo[(i, pre)]
        res = self.dfs(nums, memo, i + 1, pre)
        if nums[i] > pre:
            res = max(res, 1 + self.dfs(nums, memo, i + 1, nums[i]))
        memo[(i, pre)] = res
        return res
