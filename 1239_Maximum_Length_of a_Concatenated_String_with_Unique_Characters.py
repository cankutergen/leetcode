import string

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        result = 0
        
        def max_unique(index, current):
            nonlocal result
            if index == len(arr) and unique_char_count(current) > result:
                result = len(current)
                return
            
            if index == len(arr):
                return
            
            max_unique(index + 1, current)
            max_unique(index + 1, current + arr[index])
                
                
        def unique_char_count(current):
            counts = [0] * 26
            
            values = dict()
            for index, letter in enumerate(string.ascii_lowercase):
                values[letter] = index
            
            for char in current:
                if counts[values[char]] > 0:
                    return -1
                
                counts[values[char]] += 1
            
            return len(current)
        
        max_unique(0, "")
        return result
        
        
                
