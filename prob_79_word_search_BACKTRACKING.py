from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        visited = [[False for col in range(cols)] for row in range(rows)]
        
        def solution(row, col, ans, w):
        
            if ans == word:
                return True
            
            if (row >= rows) or (row < 0) or (col >= cols) or (col < 0):
                return False
            
            if visited[row][col] or w[0] != board[row][col]:
                return False
            
            visited[row][col] = True
            
            result = solution(row+1, col, ans+board[row][col], w[1:]) \
                or solution(row-1, col, ans+board[row][col], w[1:]) \
                or solution(row, col+1, ans+board[row][col], w[1:]) \
                or solution(row, col-1, ans+board[row][col], w[1:])
            visited[row][col] = False    
            return result
        
        for row in range(rows):
            for col in range(cols):
                if solution(row, col, "", word):
                    return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
# board = [["C","A","B"]]
# word = "EE"
board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word="AAB"
s = Solution()
print(s.exist(board,word))
