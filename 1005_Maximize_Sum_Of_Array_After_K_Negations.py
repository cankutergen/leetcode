class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:  
        for i in range(K):
            target = min(A)
            A.remove(target)
            A.append(-target)
        return sum(A) 
