class Solution(object):
    def kInversePairs1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod = 100000007
        dp = [[-1 for i in range(k+1)] for j in range(n+1)]
        # for i in range(0, n+1):
        #     dp[i][0] = 1
        # for j in range(1, k+1):
        #     dp[0][i] = 0
        # for i in range(1, n+1):
        #     for j in range(k+1):
        #         dp[i][j] = dp
        def count(n, k):
            if k == 0:
                return 1
            if n == 0:
                return 0
            if dp[n][k] != -1:
                return dp[n][k]
            inv = 0
            for i in range(min(k+1, n)):
                inv = (inv + count(n-1, k-i))%mod
            dp[n][k] = inv
            return inv
        res = count(n, k)
        return res

    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod = 100000007
        dp = [[0 for j in range(k+1)] for i in range(n+1)]

        for j in range(k+1):
            dp[0][j] = 0
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, k+1):
                for l in range(min(j,i)+1):
                    dp[i][j] = (dp[i][j] + dp[i-1][j-l]) % mod
        return dp[i][j]

s = Solution()
print(s.kInversePairs(3, 1))



