class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == None or len(nums) is 0:
            return 0
        
        if len(nums) is 1:
            return nums[0]
        
        if len(nums) is 2:
            return max(nums)
        
        dp = [None] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(dp)):
            # getting the last two houses or
            # getting the prev
            # 3d case
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
                    
        return dp[len(nums) - 1]
