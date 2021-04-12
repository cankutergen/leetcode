class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums) - k  
        nums[:] = nums[n:] + nums[:n]
