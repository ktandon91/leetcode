# TODO: Can also be solved using floyd's cycle detection

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = {1}
        new_num = 0
        while True:
            new_num = 0
            while n > 0:
                r = n%10
                new_num += r**2
                n = n//10
            if new_num in s:
                break
            s.add(new_num)
            n = new_num
        return new_num == 1

s = Solution()
print(s.isHappy(2))
