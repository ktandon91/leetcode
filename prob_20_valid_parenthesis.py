class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        matches = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for ch in s:
            if ch in "({[":
                arr.append(ch)
            if ch in "]})" and arr:
                ele = arr.pop()
                if matches[ch] != ele:
                    return False
            elif ch in "]})" and not arr:
                return False
        if not arr:
            return True
        else:
            return False

s = Solution()
print(s.isValid("()"))