class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dp(index, memo):
            if index == 0:
                return 1
            
            start_index = len(s) - index
            if s[start_index] == "0":
                return 0
            
            if index in memo:
                return memo[index]
            
            result = dp(index - 1, memo)
            if index >= 2 and int(s[start_index : start_index + 2]) <= 26:
                result += dp(index - 2, memo)
                
            memo[index] = result
            return result
        
        return dp(len(s), {})
