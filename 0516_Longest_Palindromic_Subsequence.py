class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        def dp(left, right, count):
            if left > right:
                return count  
                    
            if left == right:
                return count + 1
            
            if s[left] == s[right]:
                return dp(left + 1, right - 1, count + 2)
            else:
                res1 = dp(left + 1, right, count)
                res2 = dp(left, right - 1, count)

                return max(res1, res2)
        
        count = dp(0, len(s) - 1, 0)
        return count
