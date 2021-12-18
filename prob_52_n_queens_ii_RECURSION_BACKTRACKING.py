class Solution:
    def totalNQueens(self, n: int) -> int:
        grid = [[0 for col in range(n)] for row in range(n)]
        result = 0
        def is_safe(r, c):
            # a. check left diagnol
            checking_range = min(r,c) + 1
            for i in range(1, checking_range):
                if grid[r-i][c-i] == 1:
                    return False
            
            # b. check for straight up
            checking_range = r + 1
            for i in range(1, checking_range):
                if grid[r-i][c] == 1:
                    return False
            
            # c. checking for right diagnol
            checking_range = min(r, n-c-1) + 1
            for i in range(1, checking_range):
                if grid[r-i][c+i] == 1:
                    return False
        
            return True
                
        
        def recursive_solution(row):
            nonlocal result
            if row == n:
                result+=1
                return 
            
            for col in range(n):
                if is_safe(row, col):
                    grid[row][col] = 1
                    recursive_solution(row+1)
                    grid[row][col] = 0
            
        recursive_solution(0)
        return result
                
        