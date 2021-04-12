class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
            
        for key in dict:
            if dict[key] == 1:
                return s.index(key)
            
        
        return -1
