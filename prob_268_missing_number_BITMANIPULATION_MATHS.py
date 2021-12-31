from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Maths
        n_sum = sum(range(1, len(nums)+1))
        available_sum = sum(nums)
        return n_sum - available_sum
        # Bitwise
        # a = 0
        # b = 0
        # n = len(nums)
        # for i in range(1, n+1):
        #     a ^=i
        # for i in nums:
        #     b ^= i
        # return a^b
