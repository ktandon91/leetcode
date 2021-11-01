class Solution:
    def isValidSudoku(self, board) -> bool:
        def condition_one():
            for row in board:
                d = {}
                for element in row:
                    if element != ".":
                        if element in d:
                            return False
                        else:
                            d[element]=element
            return True
        
        def condition_two():
            for col in range(9):
                d = {}
                for row in range(9):
                    if board[row][col] != ".":
                        if board[row][col] in d:
                            return False
                        else:
                            d[board[row][col]]=board[row][col]
            return True
        
        def condition_three(r, c):
            d = {}
            for i in range(0, 3):
                for j in range(0, 3):
                    element = board[r+i][c+j]
                    if element != ".":
                        if element in d:
                            return False
                        else:
                            d[element]=element
            return True
        
        def verify(r, c):
            if r > len(board) - 1 or c > len(board[0]) -1:
                return True
            
            if not condition_three(r, c):
                return False
            
            sub1 = verify(r, c+3)
            sub2 = verify(r+3, c)
            
            if sub1 and sub2:
                return True
            return False
        
        return verify(0, 0) if (condition_one() and condition_two()) else False

s = Solution()
example = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
example2 = [
["7",".",".",".","4",".",".",".","."],
[".",".",".","8","6","5",".",".","."],
[".","1",".","2",".",".",".",".","."],
[".",".",".",".",".","9",".",".","."],
[".",".",".",".","5",".","5",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".","2",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]
]
example3 = [
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]

print(s.isValidSudoku(example))