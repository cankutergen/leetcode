class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        num_ships = 0
        
        def sink(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != "X":
                return
            
            board[i][j] = "."
            sink(i + 1, j)
            sink(i - 1, j)
            sink(i, j + 1)
            sink(i, j - 1)
            

        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "X":
                    num_ships += 1
                    sink(i, j)
                    
        return num_ships
