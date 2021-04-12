class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = []
        sorted_str = []
        dict = {}

        for current in strs:
            chars = list(current)
            chars.sort()
            sorted = "".join(chars)

            if sorted not in dict:
                dict[sorted] = []

            dict[sorted].append(current)

        for key in dict:          
            grouped.append(dict[key])

        return grouped
