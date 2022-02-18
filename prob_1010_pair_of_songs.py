from collections import defaultdict
from typing import List

# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         dp = defaultdict(int)
#         result = 0
#         for t in time:
#             new_key = t%60
#             key = (60-new_key) if new_key != 0 else 0
#             if key in dp:
#                 result+=dp[key]
#             dp[new_key]+=1
#         return result

class Solution:
    def numPairsDivisibleBy60(self, time):
        c = [0] * 60
        res = 0
        for t in time:
            res += c[-t % 60]
            c[t % 60] += 1
        return res
        
test_case = [30,20,150,100,40]
print(Solution().numPairsDivisibleBy60(test_case))
