class Solution:
    def solveNQueens(self, n: int):
        # 1. Create n x n board
        board  = [["." for row in range(0, n)] for row in range(0, n)]
        # 2. Result list
        result = []
        
        
        # 3. Function to translate board state to requisite output format.
        def translate_board_to_list():
            # Board is in 2D array convert the state to list of strings as required by the problem statement
            intermediate_result = []
            for row in range(n):
                s = "".join(board[row])
                intermediate_result.append(s)
            return intermediate_result
              
        
        # 4. Function to check if current position of the queen is safe respective of queens placed in above rows
        def is_position_safe(r, c):
            # a. check left diagnol
            checking_range = min(r,c) + 1
            for i in range(1, checking_range):
                if board[r-i][c-i] == "Q":
                    return False
            
            # b. check for straight up
            checking_range = r + 1
            for i in range(1, checking_range):
                if board[r-i][c] == "Q":
                    return False
            
            # c. checking for right diagnol
            checking_range = min(r, n-c-1) + 1
            for i in range(1, checking_range):
                if board[r-i][c+i] == "Q":
                    return False
        
            return True
        
        # 5. Recursive function to check the board
        def place_queens(row):
            # a. Base condition, if we have reached here that means all the rows have queens on them and translate the current state of the board to the requisite output by calling the translate_to_list function
            if row == n:
                result.append(translate_board_to_list())  
                return
            
            # b. placing the queen and checking for every row and column
            for col in range(n):
                # c. check if position is safe
                if is_position_safe(row, col):
                    # d. place the queen
                    board[row][col] = "Q"
                    # e. if position is safe move to next row
                    place_queens(row+1)
                    # f. Remove the queen from current position for next position check
                    board[row][col] = "."
        
        #6. Call recusive function
        place_queens(0)
        
        #7 . Return result
        return result
