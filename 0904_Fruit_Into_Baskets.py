class Solution:
    def totalFruit(self, tree: List[int]) -> int:     
        if tree is None or len(tree) is 0:
            return 0
        
        max_number = 1
        dict = {}
        i = 0
        j = 0
            
        while j < len(tree):
            if len(dict) <= 2:
                dict[tree[j]] = j
                j += 1
            
            if len(dict) > 2:
                min_index = len(tree) - 1
                for val in dict.values():
                    min_index = min(min_index, val)
                    
                i = min_index + 1
                del dict[tree[min_index]]
        
            
            max_number = max(max_number, j - i)
            
        return max_number
                
