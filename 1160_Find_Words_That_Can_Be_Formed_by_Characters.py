class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        for word in words:
            dict = {}
            for char in chars:
                if char in dict: 
                    dict[char] += 1
                else: 
                    dict[char] = 1
             
            temp = 0
            for l in word:
                if l in dict and dict[l] > 0:
                    dict[l] -= 1 
                    temp += 1
                else:
                    temp = 0
                    break
                    
            total += temp
            
        return total
