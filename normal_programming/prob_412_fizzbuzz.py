class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(n):
            new_n = i+1
            if new_n%3==0 and new_n%5==0:
                ans.append("FizzBuzz")
            elif new_n%3==0:
                ans.append("Fizz")
            elif new_n%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(new_n))
        return ans


print(None and None.left)
