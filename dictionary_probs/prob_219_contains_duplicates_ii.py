# Time O(n)
# Space O(n)

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}

        for idx, n in enumerate(nums):
            if n in d and idx - d[n] <= k:
                return True
            d[n]=idx
        return False
