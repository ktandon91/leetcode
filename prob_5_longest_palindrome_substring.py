class Solution:
    def __init__(self):
        self.dp = []
        self.max_ans = ""

    def longestPalindrome(self, s: str) -> str:
        self.dp = [[-1 for i in range(len(s) + 1)] for j in range(len(s) + 1)]
        result = self.recursive_solution(s, 0, len(s)-1)
        return result

    def is_palindrome(self, s, start, end):
        start_idx = start
        end_idx = end
        while start_idx < end_idx:
            if s[start_idx] != s[end_idx]:
                return False
            end_idx -= 1
            start_idx += 1
        return True

    def recursive_solution(self, s, start, end):
        if start > end:
            return ""
        elif start == end:
            return s[start]
        elif self.is_palindrome(s, start, end):
            return s[start:end+1]

        if self.dp[start][end] != -1:
            return self.dp[start][end]

        for k in range(start, end):
            self.dp[start][k] = self.recursive_solution(s, start, k)
            self.dp[k + 1][end] = self.recursive_solution(s, k + 1, end)
            temp_ans = max(self.dp[start][k], self.dp[k + 1][end], key=len)
            self.max_ans = max(self.max_ans, temp_ans, key=len)
        return self.max_ans

s = Solution()
result = s.longestPalindrome("cbbd")
print(result)
