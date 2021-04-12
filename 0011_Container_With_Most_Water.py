class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        i = 0
        j = len(height) - 1
        
        while i < j:
            minimum = min(height[i], height[j])
            maximum = max(maximum, minimum * (j - i))
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return maximum
