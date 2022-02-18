from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        d = {}
        sum_=0
        for n in nums:
            new_key = (sum_+n)%3
            key = 3-new_key
            if key == 3:
                sum_+=n
            elif key in d:
                sum_+=(d[key]+n)
                del d[key]
            else:
                d[new_key]=n
        return sum_

print(Solution().maxSumDivThree([3,6,5,1,8]))
