class Solution:
    def letterCombinations(self, digits: str):
        base_ascii = ord('a')
        results = []
        
        def pad(p, up):
            if not up:
                if p:
                    results.append(p)
                return 

            digit = int(up[0])

            if digit < 2:
                start, end = 0, 0
            if digit >=2 and digit < 7:
                start = (digit-2)*3
                end = start+3
            if digit == 7:
                start = (digit-2) * 3
                end = start + 4
            if digit == 8:
                start = (digit-2) * 3 + 1
                end = start + 3
            if digit == 9:
                start = (digit-2)*3 + 1
                end = start + 4
            for i in range(start, end):
                ch = chr(base_ascii + i)
                pad(p+ch, up[1:])
        
        pad("", digits)
        return results

s = Solution()
print(s.letterCombinations("9"))