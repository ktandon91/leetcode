class Solution(object):
    def climbStairs2(self, num):
        """
        :type n: int
        :rtype: int
        """
        if num == 0:
            return 0
        dp = [-1 for _ in range(num)]
        def sol(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if dp[n-1] != -1:
                return dp[n-1]
            dp[n-1] = sol(n-1) + sol(n-2)
            return dp[n-1]
        sol(num)
        return dp[num-1]

    def climbStairs(self, n):
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]

    def climbStairs(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        curr = 2
        prev = 1
        for i in range(2, n):
            t = curr
            curr = curr + prev
            prev = t
        return curr

s = Solution()
print(s.climbStairs(8))
