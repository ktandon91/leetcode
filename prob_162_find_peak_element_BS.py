class Solution:
    def findPeakElement(self, nums) -> int:
        start = 0
        end = len(nums) - 1
        peak_idx = -1
        peak_ans = float('-inf')
        while start <= end:
            if start == end:
                if peak_ans < nums[start]:
                    peak_idx = start
                    peak_ans = nums[start]
                end-=1
            mid = (start + end) // 2
            if (mid < end):
                if nums[mid] > nums[mid + 1]:
                    if peak_ans < nums[mid]:
                        peak_ans = nums[mid]
                        peak_idx = mid
                    end = mid - 1
                else:
                    start = mid + 1
            elif (mid > start):
                if nums[mid - 1] > nums[mid]:
                    peak_idx = mid - 1
        return peak_idx

s= Solution()
print(s.findPeakElement([1,2,1,3,5,6,4]))