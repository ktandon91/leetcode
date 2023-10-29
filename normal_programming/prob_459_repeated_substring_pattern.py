class Solution(object):
    def repeatedSubstringPattern1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s) # n = 4
        if n == 1:
            return False

        h = n//2
        if n%2 != 0:
            h = h+1   # h = 2  indices 0,1,2,3

        res = False
        for i in range(1, h+1):
            if n%i != 0:
                continue
            
            for j in range(0,n-i,i):
                res = (s[j:j+i] == s[j+i:j+2*i])
                if not res:
                    break
            if res:
                break
        return res


    def repeatedSubstringPattern(self, s):

        """
        :type str: str
        :rtype: bool
        """
        if not s:
            return False
            
        ss = (s + s)[1:-1]
        return ss.find(s) != -1
        
     
s = Solution()
print(s.repeatedSubstringPattern("ababc"))
