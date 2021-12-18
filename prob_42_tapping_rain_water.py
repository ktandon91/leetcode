class Solution:
    def trap(self, height) -> int:
        left = 0
        right = len(height)-1
        left_max, right_max, ans = 0, 0, 0
        
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans = ans + left_max-height[left]
                left+=1
            elif height[left] >= height[right]:
                right_max = max(right_max, height[right])
                ans = ans +  right_max-height[right]
                right-=1
        
        return ans

test_case = [0,1,0,2,1,0,1,3,2,1,2,1]
s= Solution()
print(s.trap(test_case))
