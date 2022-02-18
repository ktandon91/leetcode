# Levenshtein distance Here is the link to wiki: https://en.wikipedia.org/wiki/Levenshtein_distance
class Solution:
    def minDistanceRecursive(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = {}
        def solve(i,j):
            if i==n and j==m:
                return 0
            
            if i==n:
                return m-j
            
            if j==m:
                return n-i
            
            if (i, j) in dp:
                return dp[(i,j)]
            
            if word1[i] == word2[j]:
                dp[(i,j)] = solve(i+1, j+1)
            else:
                delete = 1+solve(i+1, j)
                insert = 1+solve(i,j+1)
                replace = 1+solve(i+1,j+1)
                dp[(i,j)] = min(delete, insert, replace)
            return dp[(i,j)]
        return solve(0,0)
    
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        
        for i in range(1,n+1):
            for j in range(1, m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(1+dp[i-1][j], 1+dp[i][j-1],1+dp[i-1][j-1])
        return dp[-1][-1]
s1= "intention"
s2 = "execution"
print(Solution().minDistance(s1,s2))
