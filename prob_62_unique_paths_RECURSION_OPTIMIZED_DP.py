class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[0 for col in range(n)] for row in range(m)]
        def recursive_solution(r, c):
            if r == m-1 and c==n-1:
                return 1
            
            if r > m-1 or c > n-1:
                return 0
            
            if board[r][c] != 0:
                return board[r][c]
            
            board[r][c] = recursive_solution(r+1, c) + recursive_solution(r, c+1)

            return board[r][c]
        return recursive_solution(0,0)
