# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         stack = []
#         counter, max_len = 0, 0
#         running_length = 0
#         for ch in s[::-1]:
#             if ch == ")":
#                 stack.append(")")
#             elif ch == "(" and stack:
#                 stack.pop()
#                 counter+=2
#                 if not stack:
#                     running_length+=counter
#                     max_len=max(running_length, max_len)
#                     counter=0
#                 else:
#                     max_len=max(max_len, counter)
#             elif ch == "(" and not stack:
#                 # max_len = max(max_len, counter)
#                 counter=0
#                 running_length=0
#         if stack:
#             max_len=max(max_len, counter)
        
#         return max_len

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for idx, ch in enumerate(s):
            if ch == ")" and stack:
                if (stack[-1] != -1) and (s[stack[-1]] == "("):
                    stack.pop()
                else:
                    stack.append(idx)
            else:
                stack.append(idx)
        
        stack.append(len(s))
        for i in range(1, len(stack)):
            l = stack[i]-stack[i-1] - 1
            max_len = max(max_len, l)
            
        return max_len

s=Solution()
test_case = ")()())()()("
test_case2= "()"
test_case3 = "()(()"
test_case4 = "(()"
test_case5 = "(()))())("
test_case6="(()))())("
print(s.longestValidParentheses(test_case6))
