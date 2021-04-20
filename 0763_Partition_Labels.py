class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        dict = {}
        for i, char in enumerate(S):
            dict[char] = i

        left, right = 0, 0


        result = []
        for i, char in enumerate(S):

            right = max(right, dict[char])

            if i == right:
                result += [right - left + 1]
                left = i + 1

        return result
