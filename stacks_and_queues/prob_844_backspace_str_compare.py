class Solution(object):
    def backspaceCompare2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        wc_s = []
        wc_t = []

        for c in s:
            if c == "#" and wc_s:
                wc_s.pop()
            if c != "#":
                wc_s.append(c)
        
        for c in t:
            if c == "#" and wc_t:
                wc_t.pop()
            if c != "#":
                wc_t.append(c)
        
        return wc_s == wc_t
    
    def backspaceCompare(self, S, T):
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1

s = Solution()
print(s.backspaceCompare("ab#c", "ad#c"))
