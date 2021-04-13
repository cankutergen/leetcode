class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            square = nums[i]**2
            nums[i] = square
            
        nums.sort()
        return nums
