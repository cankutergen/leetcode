class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        set_num = set()
        
        for i in nums:
            set_num.add(i)
            
        for i in range(len(nums) + 1):
            if i not in set_num:
                return i
            
        return -1
            
