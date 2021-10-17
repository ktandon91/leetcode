class Solution:
    def peakIndexInMountainArray(self, arr):
        start = 0
        end = len(arr) - 1
        temp_ans = float('-inf')
        ans = -1
        while start <= end:
            mid = (start+end)//2
            if arr[mid] > arr[mid+1]:
                if temp_ans < arr[mid]:
                    ans = mid
                    temp_ans = arr[mid]
                end = mid - 1
            else:
                start = mid + 1
        return ans


s = Solution()
print(s.peakIndexInMountainArray([0,10,5,2]))
