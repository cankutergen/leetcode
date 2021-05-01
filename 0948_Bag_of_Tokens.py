class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        
        max_points = 0
        points = 0
        left = 0
        right = len(tokens) - 1
        
        while left <= right:
            if P >= tokens[left]:
                points += 1
                P -= tokens[left]
                left += 1
                max_points = max(max_points, points)
            elif points > 0:
                points -= 1
                P += tokens[right]
                right -= 1
            else:
                return max_points
            
        return max_points
            
                
                
