class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                return num
