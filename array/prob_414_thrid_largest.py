from typing import List
import math

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f = float('-inf')
        s = float('-inf')
        t = float('-inf')
        l = len(nums)
        if l < 3:
            return max(nums)
        for n in nums:
            if n == f or n == s or n == t:
                continue
            if n > f:
                t = s
                s = f
                f = n
            elif n > s:
                t = s
                s = n
            elif n > t:
                t = n
        return t if not math.isinf(t) else f

s = Solution()
print(s.thirdMax([1,2,-2147483648]))