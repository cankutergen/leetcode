class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        if strs is None or len(strs) is 0:
            return res
        
        index = 0
        for c in strs[0]:
            for i in range(1, len(strs)):
                if index >= len(strs[i]) or c != strs[i][index]:
                    return res
            
            res += c   
            index += 1
            
        return res
