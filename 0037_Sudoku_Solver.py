class Solution:
    def solveSudoku(self, board: List[List[str]]):
        # step 1: choose somewhere on the puzzle to make a guess
        row, col = self.find_next_empty(board)

        # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
        if row is None:  # this is true if our find_next_empty function returns None, None
            return True 

        # step 2: if there is a place to put a number, then make a guess between 1 and 9
        for guess in range(1, 10): # range(1, 10) is 1, 2, 3, ... 9
            # step 3: check if this is a valid guess
            if self.is_valid(board, guess, row, col):
                # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
                board[row][col] = str(guess)
                # step 4: then we recursively call our solver!
                if self.solveSudoku(board):
                    return True

            # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
            board[row][col] = "."

        # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
        return False
        
    
    def find_next_empty(self, puzzle):
        # finds the next row, col on the puzzle that's not filled yet --> rep with -1
        # return row, col tuple (or (None, None) if there is none)

        # keep in mind that we are using 0-8 for our indices
        for r in range(9):
            for c in range(9): # range(9) is 0, 1, 2, ... 8
                if puzzle[r][c] == ".":
                    return r, c

        return None, None  # if no spaces in the puzzle are empty (-1)

    def is_valid(self, puzzle, guess, row, col):
        # figures out whether the guess at the row/col of the puzzle is a valid guess
        # returns True or False

        # for a guess to be valid, then we need to follow the sudoku rules
        # that number must not be repeated in the row, column, or 3x3 square that it appears in

        # let's start with the row
        row_vals = puzzle[row]
        if str(guess) in row_vals:
            return False # if we've repeated, then our guess is not valid!

        # now the column
        # col_vals = []
        # for i in range(9):
        #     col_vals.append(puzzle[i][col])
        col_vals = [puzzle[i][col] for i in range(9)]
        if str(guess) in col_vals:
            return False

        # and then the square
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3

        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if puzzle[r][c] == str(guess):
                    return False

        return True
