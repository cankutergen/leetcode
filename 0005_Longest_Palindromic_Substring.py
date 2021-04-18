class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if s == None or len(s) < 1: 
            return ""

        res = ""
        resLen = 0

        def expand(left, right, res, resLen):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resLen:
                    res = s[left: right + 1]
                    resLen = right - left + 1

                left -= 1
                right += 1

            return (res, resLen)


        for i in range(len(s)):

            # odd length
            left, right = i, i
            res, resLen = expand(i, i, res, resLen)
           
            # even length
            left, right = i, i + 1
            res, resLen = expand(i, i + 1, res, resLen)

        return res  
