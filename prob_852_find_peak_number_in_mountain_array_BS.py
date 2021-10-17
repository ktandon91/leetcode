class Solution:
    def peakIndexInMountainArray(self, arr):
        start = 0
        end = len(arr) - 1
        ans = float('-inf')
        while start < end:
            mid = (start+end)//2
            if arr[mid] > arr[mid+1]:
                ans = max(ans, arr[mid])
                end = mid - 1
            else:
                start = mid + 1
        if start == end:
            ans = max(ans, arr[start])
        return ans


s = Solution()
print(s.peakIndexInMountainArray([3,4,5,6,1,2]))
