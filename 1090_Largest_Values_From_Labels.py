from heapq import heappop, heappush, heapify

        # N logn(N)
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        max_heap = []
        heapify(max_heap)
        
        for i in range(len(labels)):
            heappush(max_heap, (-values[i], labels[i]))

        counts = {}
        result = 0
        
        while max_heap and num_wanted > 0:
            val, label = heappop(max_heap)
            
            if label not in counts:
                counts[label] = 1
            else:
                counts[label] += 1
            
            if counts[label] <= use_limit:
                result += -val
                num_wanted -= 1
                
        return result
