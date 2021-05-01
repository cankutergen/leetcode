class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeated_subsequences = set()
        seen = {}
        
        left = 0
        while left + 10 <= len(s):
            subsequence = s[left: left + 10]
            left += 1
            
            if subsequence not in seen:
                seen[subsequence] = 1
            else:
                repeated_subsequences.add(subsequence)
                
        return repeated_subsequences
