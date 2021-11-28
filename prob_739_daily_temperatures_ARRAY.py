class Solution:
    def dailyTemperatures(self, temperatures):
        if len(temperatures) == 1:
            return [0]
        left, right = 0,0
        ans = []
        while left < len(temperatures):
            if right >= len(temperatures):
                ans.append(0)
                left+=1
                right = left
            elif temperatures[right] > temperatures[left]:
                ans.append(right-left)
                left+=1
                right = left
            else:
                right+=1
        return ans
        
s = Solution()
example1 = [73,74,75,71,69,72,76,73]
example2 = [30,40,50,60]
print(s.dailyTemperatures(example2))
