class Solution:
    def maxUncrossedLinesRecursive(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        
        def solve(i, j):
            if i == n or j == m:
                return 0
            
            if nums1[i] == nums2[j]:
                return 1+solve(i+1, j+1)
            
            else:
                return max(solve(i+1,j), solve(i, j+1))
            
        return solve(0, 0)
    
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [ [0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for j in range(m+1):
            dp[0][j] = 0
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
