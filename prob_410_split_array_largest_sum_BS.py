class Solution:
    def splitArray(self, nums, m) -> int:
        start = 0
        end = 0
        for num in nums:
            start = max(start, num)
            end += num

        while start < end:
            mid = (start + end)//2
            i_sum = 0
            pieces = 1
            for num in nums:
                if i_sum + num > mid:
                    i_sum=num
                    pieces+=1
                else:
                    i_sum+=num

            if pieces > m:
                start = mid + 1
            else:
                end = mid
        return end

s = Solution()
print(s.splitArray([7,2,5,10,8],2))