class Solution:
    def romanToInt1(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        stack = []
        for c in s:
            if stack:
                if stack[-1] >= d[c]:
                    stack.append(d[c])
                else:
                    new_sum = d[c]
                    while stack and stack[-1] < d[c]:
                        element = stack.pop()
                        new_sum-=element
                    stack.append(new_sum)
            else:
                stack.append(d[c])
        
        final_value = 0
        for c in stack:
            final_value+=c
        
        return final_value

    #TODO : Complete this
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        integer_value = 0
        left, right = 0, 1
        
        if len(s) == 1:
            return d[s[0]]
        
        while right <= len(s)-1:
            if d[s[left]] >= d[s[right]]:
                integer_value+=d[s[left]]
                left+=1
                right+=1
            else:
                integer_value+=(d[s[right]]-d[s[left]]) 
                left+=2
                right+=2
        return integer_value

test_case = "MCMXCIV"
s = Solution()
print(s.romanToInt("III"))
