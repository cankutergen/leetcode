class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        minSwaps = min(self.numSwaps(A[0], A, B), self.numSwaps(B[0], A, B), self.numSwaps(A[0], B, A), self.numSwaps(B[0], B, A))
        
        if minSwaps == sys.maxsize:
            return -1
        else:
            return minSwaps
        
        
    def numSwaps(self, target, A, B):
        swaps = 0
        for i in range(len(A)):
            if A[i] != target and B[i] != target:
                return sys.maxsize
            elif A[i] != target:
                swaps += 1
        
        return swaps
