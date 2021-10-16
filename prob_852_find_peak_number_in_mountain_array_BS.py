class Solution:
    def peakIndexInMountainArray(self, arr):
        start = 0
        end = len(arr) - 1
        ans = float('-inf')
        while start <= end:
            mid = (start+end)//2
            if arr[mid] > arr[mid+1]:
                ans = max(ans, arr[mid])
                end = mid - 1
            else:
                start = mid + 1
        return ans


s = Solution()
print(s.peakIndexInMountainArray([1,2,1]))
