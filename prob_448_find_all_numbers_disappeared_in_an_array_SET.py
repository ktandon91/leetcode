from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        nums_set = set(nums)
        for i in range(1, n+1):
            if i not in nums_set:
                result.append(i)
        return result
        