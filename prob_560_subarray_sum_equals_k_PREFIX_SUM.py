from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        n = len(nums)
        ptr = 0
        result = 0
        agg=0
        while ptr < n:
            agg += nums[ptr]
            key = agg-k
            if key in  prefix_sum:
                result += prefix_sum[key]
            prefix_sum[agg]+=1
            ptr+=1
        return result
test_case = [1,1,1]
test_case_2 = [1,2,3]
print(Solution().subarraySum(test_case_2,3))
