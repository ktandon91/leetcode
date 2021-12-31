class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        # Find the last ascending index from right of the array
        while i > 0 and nums[i-1] >= nums[i]:
            i-=1
        # If i == 0 that means the array is in descending order and
        # there is no other solution greater than current formation is possible
        # Therefore, reverse the array and return
        if i == 0:
            nums.reverse()
            return
        # k will be the index of element just before last ascending
        k = i - 1
        j = n-1
        # Starting from end find the first largest value than k
        while nums[j] <= nums[k]:
            j-=1
        nums[j], nums[k] = nums[k], nums[j]
        # Reverse the elements from k+1 till end
        l, r = k+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        