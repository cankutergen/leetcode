class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        nums.sort()
        
        def backtrack(index, curr, nums):
            if curr not in subset:
                subset.append(curr.copy())
            
            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr, nums)
                curr.pop()
        
        backtrack(0, [], nums)
        return subset
