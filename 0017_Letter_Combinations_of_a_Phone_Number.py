class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = list()
        if digits == None or len(digits) == 0:
            return result
        
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        self.dfs(result, digits, "", 0, mapping)
        return result
        
    def dfs(self, result, digits, current, index, mapping):
        #no numbers to process
        if index == len(digits):
            result.append(current)
            return
        
        letters = mapping[int(digits[index])]
        for i in range(len(letters)):
            self.dfs(result, digits, current + letters[i], index + 1, mapping)
