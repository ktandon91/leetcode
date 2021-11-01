class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """   
        i = m - 1
        j = n - 1
        k = m + n - 1
        # nums1 : m, nums2 : n
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
         
        # don't need to do this for i, as in nums1 list only we are storing so they are               already in their correct positions
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


s= Solution()
print(s.merge([1,2,3,7,0,0], 4, [2,5,6], 3))