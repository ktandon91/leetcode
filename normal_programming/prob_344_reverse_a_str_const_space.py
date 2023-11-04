class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        st = 0
        ed = len(s) - 1
        while st < ed:
            s[ed], s[st] = s[st], s[ed]
            st += 1
            ed -= 1
        return s
