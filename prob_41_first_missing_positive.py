from typing import List

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within 
            the range [1,...,l+1] 
        """
        nums.append(0)
        nums2 = nums.copy()
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]//n==0:
                return i
        return n

    def firstMissingPositiveNonConstantSpace(self, nums: List[int]) -> int:
        nums_set = set(nums)
        min_positive = float('inf')
        for num in nums:
            if num > 0 and num < min_positive:
                min_positive = num   
        if min_positive > 1:
            return 1
        while min_positive in nums_set:
            min_positive+=1
        return min_positive

s = Solution()
test_case = [5,4,3,0,1]
test_case2 = [2,2]
test_case3 = [4,5,1,0,2]
print(s.firstMissingPositive(test_case3))
