class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        dp = {}
        def minimum_cost(stair, c):
            if stair == len(cost):
                return c
            if stair >= len(cost):
                return float('inf')
            
            if stair in dp:
                if dp[stair] < c:
                    return float('inf')
            if stair == -1:
                cost_to_pass = c
            else:
                cost_to_pass = c+cost[stair]
            one_step = minimum_cost(stair+1, cost_to_pass)
            two_step = minimum_cost(stair+2, cost_to_pass)
        
            dp[stair] = min(one_step, two_step)
        
            return dp[stair]

        result = minimum_cost(-1, 0)
        return result