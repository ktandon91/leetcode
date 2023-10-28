class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h = len(haystack)
        n = len(needle)
        
        if n > h:
            return -1

        n_fch = needle[0]
        for idx, ch in enumerate(haystack):
            if idx + n <= h:
                if ch == n_fch and needle == haystack[idx: idx+n]:
                    return idx
        return -1 

    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h = len(haystack)
        n = len(needle)
        
        if n > h:
            return -1

        hash_n = hash(needle)
        for idx in range(0, h-n+1):
            if hash(haystack[idx:idx+n]) == hash_n:
                return idx
        
        return -1
