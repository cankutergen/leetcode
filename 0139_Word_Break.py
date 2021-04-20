class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set(wordDict) 
        size = len(s)
        
        def dfs(start, s, wordSet, size, memo):
            if start >= size:
                return True

            if start in memo:
                return memo[start]
            
            for i in range(start, size):
                if s[start: i + 1] in wordDict:
                    memo[start] = dfs(i + 1, s, wordSet, size, memo)
                    if memo[start]:
                        return True
                   
            return False
            
        memo = {}
        return dfs(0, s, wordSet, size, memo)
