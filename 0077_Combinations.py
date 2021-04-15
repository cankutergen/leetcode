class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        sol = []
        def backtrack(remain, comb, next):
            # find solution
            if remain == 0:
                sol.append(comb.copy())
            else:
                for i in range(next, n + 1):
                    # add candidate
                    comb.append(i)
                    
                    # recurse
                    backtrack(remain - 1, comb, i + 1)
                    
                    # backtrack
                    comb.pop()
                    
        backtrack(k, [], 1)
        return sol
