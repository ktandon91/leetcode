class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r*r > num:
            r = (r+num/r)//2
        return r*r == num

s = Solution()
print(s.isPerfectSquare(169))
