class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0
        
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            # compute sum for previous subarray
            curr_sum += num
            
            # if current sum <= the current number,
            # no need to include previous subarray
            if curr_sum <= num:
                curr_sum = num
                
            max_sum = max(max_sum, curr_sum)  
        return max_sum
        
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))