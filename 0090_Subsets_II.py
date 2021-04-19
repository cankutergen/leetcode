class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        
        return res
    
    def dfs(self, nums, index, path, res):
        res.append(path.copy())
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            
            path.append(nums[i])
            self.dfs(nums, i+1, path, res)
            path.pop()
