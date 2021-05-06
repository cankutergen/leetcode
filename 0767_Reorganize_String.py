from heapq import heappush, heappop, heapify

class Solution:
    def reorganizeString(self, S: str) -> str:
        counts = {}
        for char in S:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
                
        max_heap = []
        heapify(max_heap)
        
        # count the occurence and create a list to heapify, default is minheap but we want maxheap so put a minus sign
        for key, value in counts.items():
            heappush(max_heap, (-value, key))
          
        result = ""
        while len(max_heap) > 1:
            current_count, current_char = heappop(max_heap)
            next_count, next_char = heappop(max_heap)
            
            result += current_char
            result += next_char  
            
            counts[current_char] -= 1
            counts[next_char] -= 1
            
            if counts[current_char] > 0:
                heappush(max_heap, (current_count + 1, current_char))
                            
            if counts[next_char] > 0:
                heappush(max_heap, (next_count + 1, next_char))
        
        
        if len(max_heap) > 0:
            last_count, last_letter = heappop(max_heap)
            if counts[last_letter] > 1:
                return ""
            
            result += last_letter
            
        return result
