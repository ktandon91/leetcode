class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        for divisor in [2,3,5]:
            while n % divisor == 0:
                n = n//divisor
        return n == 1
