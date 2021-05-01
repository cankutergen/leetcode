class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
            
        if total % 2 != 0:
            return False
        
        def helper(index, subset_sum, memo):
            if subset_sum * 2 == total:
                return True
            
            if subset_sum > total / 2 or index >= len(nums):
                return False
            
            if (index, subset_sum) in memo:
                return memo[(index, subset_sum)]
            
            # taking and not taking the number
            memo[(index, subset_sum)] = helper(index + 1, subset_sum, memo) or helper(index + 1, subset_sum + nums[index], memo)
            return memo[(index, subset_sum)]
        
        memo = {}
        return helper(0, 0, memo)
