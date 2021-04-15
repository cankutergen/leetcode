class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, target, curr):
            if target < 0:
                return
            
            if target == 0:
                res.append(curr.copy())
                
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                
                backtrack(i, target - candidates[i], curr)
                
                curr.pop()
        
        backtrack(0, target, [])
        return res
