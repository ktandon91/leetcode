class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lookup = set()
        for n in nums:
            if n in lookup:
                return True
            lookup.add(n)
        return False
