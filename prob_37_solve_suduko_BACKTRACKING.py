class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def is_safe(r, c, num):
            for i in range(9):
                if board[i][c]==num: return False
            
            for i in range(9):
                if board[r][i]==num: return False      

            row,col = 3*(r//3), 3*(c//3)
            for i in range(0, 3):
                for j in range(0, 3):
                    if board[row+i][col+j]== num: return False

            return True
        
        def solve(row,col):
            if row >= 9:
                return True
            if col >= 9:
                return solve(row+1, 0)
            
            if board[row][col] != ".":
                return solve(row, col+1)
            
            for num in range(1,10):
                if is_safe(row, col, str(num)):
                    board[row][col] = str(num)
                    if solve(row,col+1):
                        return True
                    board[row][col] = "."
        
        return solve(0,0)

s = Solution()
example1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(s.solveSudoku(example1))
