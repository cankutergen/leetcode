class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        matrix = []
        max_val = 0
        for i in range(len(A)):
            row = []
            for j in range(len(B)):
                if A[i] != B[j]:
                    row.append(0)
                else:
                    if i - 1 < 0 or j - 1 < 0:
                        row.append(1)
                    else:
                        val = matrix[i - 1][j - 1] + 1
                        row.append(val)
                        max_val = max(val, max_val)

            matrix.append(row)

        return max_val
