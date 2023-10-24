class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 or n < 0:
            return False
        if n == 1:
            return True
        a = n
        while a > 1:
            if a % 4 != 0:
                return False
            a = a//4
        return True

# n is positive.
# n is a power of 2. (TRICK)
# n has a remainder of 1 when divided by 3
class Solution2:
    def isPowerOfFour(self, n):
        return (n>0) and ((n&(n-1))==0) and ((n%3==1))

# Solution3
# int fac = 0b01010101010101010101010101010101; (TRICK)
# return (n>0) && ((n&(n-1))==0) && (fac&n)>0;
binary_number = 0b1101
print(binary_number)
