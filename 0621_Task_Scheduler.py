from heapq import heappush, heappop, heapify

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        max_heap = []
        heapify(max_heap)
        
        for char in tasks:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
                
        for key, value in counts.items():
            heappush(max_heap, (-value, key))
            
        cycles = 0
        while len(max_heap) > 0:
            temp = []
            
            # try to take task to process
            for i in range(n + 1):
                if max_heap:
                    count, char = heappop(max_heap)
                    temp.append((char, -count))
        
            for key, count in temp:
                count -= 1
                if count > 0:
                    heappush(max_heap, (-count, key))
                    
            if len(max_heap) == 0:
                cycles += len(temp)
            else:
                cycles += n + 1
                
        return cycles
            
 
