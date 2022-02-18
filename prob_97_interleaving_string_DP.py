class Solution:
    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        p = len(s3)
        dp = {}
        def solve(i, j):
            if i == n and j == m:
                return True
            if (i, j) in dp:
                return dp[(i,j)]
            if i < n and s1[i] == s3[i+j] and solve(i+1, j):
                return True
            if j < m and s2[j] == s3[i+j] and solve(i, j+1):
                return True
            dp[(i, j)] = False
            return False
        return solve(0,0)
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        p = len(s3)
        if n + m != p:
            return False
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[n][m] = True
        for i in range(n,-1,-1):
            for j in range(m,-1,-1):
                if i < n and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < m and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        return dp[0][0]
    
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

t1_s1 = "a"
t2_s2 = ""
t3_s3 = "a"

print(Solution().isInterleave(s1,s2,s3))
