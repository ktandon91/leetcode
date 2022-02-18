class Solution:
    def minimumDeleteSumRecursive(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        #### BASE conditions
        ### if s1 is empty return sum of ascii value of s2
        ### if s2 is empty return sum of ascii value of s1
        def solve(i, j):
            if i >=n and j >= m:
                return 0
            
            if i >= n:
                return sum([ord(ch) for ch in s2[j:]])
            
            if j >= m:
                return sum([ord(ch) for ch in s1[i:]])
            
            if s1[i]==s2[j]:
                return solve(i+1, j+1)
            else:
                return min(ord(s1[i])+solve(i+1, j),ord(s2[j])+solve(i, j+1))
        return solve(0, 0)
    
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        dp[0][0] = 0
        
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0]+ord(s1[i-1])
        
        for j in range(1, m+1):
            dp[0][j] = dp[0][j-1]+ord(s2[j-1])
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(ord(s1[i-1])+dp[i-1][j], ord(s2[j-1]) + dp[i][j-1])
        return dp[-1][-1]
            
s1 = "sea"
s2 = "eat"
print(Solution().minimumDeleteSum(s1, s2))
