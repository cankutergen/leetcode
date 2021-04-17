class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def LCS(s1, s2, i1, i2, memo):
            if len(s1) == i1 or i2 == len(s2):
                return ""

            if (i1, i2) in memo:
                return memo[(i1, i2)]

            # first chars are equal
            if(s1[i1] == s2[i2]):
                memo[(i1, i2)] = s1[i1] + LCS(s1, s2, i1 + 1, i2 + 1, memo)
                return memo[(i1, i2)]

            resA = LCS(s1, s2, i1 + 1, i2, memo)
            resB = LCS(s1, s2, i1, i2 + 1, memo)

            if(len(resA) > len(resB)):
                memo[(i1, i2)] = LCS(s1, s2, i1 + 1, i2, memo)
                return memo[(i1, i2)]
            else:
                memo[(i1, i2)] = LCS(s1, s2, i1, i2 + 1, memo)
                return memo[(i1, i2)]
                
        memo = {}
        res = LCS(text1, text2, 0, 0, memo)
        return len(res)
