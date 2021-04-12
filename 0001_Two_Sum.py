class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two pointer technique
        
        j = 1
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if target == nums[i] + nums[j]:
                    return [i, j]
                j += 1
