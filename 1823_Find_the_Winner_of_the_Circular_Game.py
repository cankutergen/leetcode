class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        arr = [x + 1 for x in range(n)]

        def run(currIndex, arr):
            if len(arr) == 1:
                return arr[0]

            removeIndex = (currIndex + k - 1) % len(arr)
            del arr[removeIndex]
            return run(removeIndex, arr)

        res = run(0, arr)
        return res 
