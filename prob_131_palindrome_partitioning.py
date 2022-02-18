from typing import List


def is_palindrome(s):
    start = 0
    end = len(s)-1
    while start < end:
        if s[start] == s[end]:
            start+=1
            end-=1
        else:
            return False
    return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        part = []
        def dfs(i):
            if i >= len(s):
                result.append(part[:])
                return 
            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return result
                

test_case = "aab"
print(Solution().partition(test_case))
