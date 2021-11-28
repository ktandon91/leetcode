class Solution:
    def minPathSum(self, grid) -> int:
        min_sum = float('inf')
        
        def recursive_solution(r,c, running_sum):
            nonlocal min_sum
            
            if r >= len(grid) or c >= len(grid[0]):
                return float('inf')
            
            running_sum = running_sum + grid[r][c]
            
            if (r == len(grid)-1) and (c == len(grid[0])-1):
                if running_sum < min_sum:
                    min_sum = running_sum
            recursive_solution(r+1,c,running_sum)
            recursive_solution(r,c+1,running_sum) 
        
        recursive_solution(0,0,0)
        return min_sum
