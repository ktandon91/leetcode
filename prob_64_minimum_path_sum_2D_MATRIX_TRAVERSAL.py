class Solution:
    def minPathSum(self, grid) -> int:
        min_sum = float('inf')
        row = len(grid) + 1
        col = len(grid[0]) + 1
        dp = [[0 for c in range(col)] for r in range(row)]
        
        for r in range(row):
            dp[r][col-1]=float('inf')
        
        for c in range(col):
            dp[row-1][c]=float('inf')
        
        dp[row-1][col-2] = 0
        for r in range(row-2,-1,-1):
            for c in range(col-2, -1, -1):
                dp[r][c] = min(dp[r+1][c]+grid[r][c], dp[r][c+1]+grid[r][c])
        
        return dp[0][0]

s= Solution()
example1 =  [[1,3,1],[1,5,1],[4,2,1]]
print(s.minPathSum(example1))
