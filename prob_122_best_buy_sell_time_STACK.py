from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        # start_idx = 0
        start, end = 0,0
        while start < n:
            start_idx, end = start, start
            loop_max_profit = 0
            while end < n:
                if prices[start] < prices[end]:
                    loop_max_profit = max(loop_max_profit, prices[end]-prices[start])
                    start_idx = end
                end+=1
            max_profit+=loop_max_profit
            start = start_idx+1
        return max_profit

s = Solution()
test_case = [7,1,5,3,6,4]
print(s.maxProfit(test_case))
