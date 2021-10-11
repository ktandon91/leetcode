class Solution:
    def longestCommonPrefix(self, strs) -> str:
        min_length = float('inf')
        longest_common = []
        common = []
        if not strs:
            return ""

        for s in strs:
            min_length = min(min_length, len(s))

        for i in range(0, min_length):
            alpha = strs[0][i]
            del_char = False
            for s in strs:
                if s[i] != alpha:
                    del_char = True
                    longest_common = max(common, longest_common, key=lambda x: len(x))
                    common = []
                    break
            if not del_char:
                common.append(alpha)
        longest_common = max(common, longest_common, key=lambda x: len(x))
        return "".join(longest_common)

s = Solution().longestCommonPrefix(["car", "cir"])
print(s)