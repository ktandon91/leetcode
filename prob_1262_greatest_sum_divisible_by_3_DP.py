from typing import List


class Solution:
    def maxSumDivThreeRecursive(self, nums: List[int]) -> int:
        n = len(nums)
        
        def solve(i, temp_sum):
            if i >= n:
                if temp_sum % 3 == 0:
                    return temp_sum
                return 0
            
            return max(solve(i+1, temp_sum+nums[i]), solve(i+1, temp_sum))
        
        return solve(0, 0)
    
    def maxSumDivThreeIterative(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        running_sum = 0
        for i in range(1, n+1):
            running_sum += nums[i-1]
            if running_sum % 3 == 0:
                dp[i] = running_sum 
            else:
                dp[i] = running_sum-nums[i-1]
    
    def maxSumDivThree(self, nums):
        dp = [0, 0, 0]
        for num in nums:
            for i in dp[:]:
                dp[(i + num) % 3] = max(dp[(i + num) % 3], i + num)
        return dp[0]

test_case1 = [3,6,5,1,8]
print(Solution().maxSumDivThree(test_case1))
