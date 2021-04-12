class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if board == None or len(board) == 0:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and self.dfs(board, i, j, 0, word):
                    return True
                
        return False
        
        
    def dfs(self, board, i, j, count, word):
        
        if count == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[count]:
            return False
        
        temp = board[i][j]
        board[i][j] = " "
        
        res1 = self.dfs(board, i + 1, j, count + 1, word)
        res2 = self.dfs(board, i - 1, j, count + 1, word)
        res3 = self.dfs(board, i, j + 1, count + 1, word)
        res4 = self.dfs(board, i, j - 1, count + 1, word)
        found = res1 or res2 or res3 or res4
        
        board[i][j] = temp
        return found
