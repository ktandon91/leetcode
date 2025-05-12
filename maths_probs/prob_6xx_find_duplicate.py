class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        expected = l*(l+1)/2
        actual = 0
        bad_num = 0
        for n in nums:
            nums[abs(n)-1] *= -1
            if nums[abs(n)-1] > 0:
                bad_num = abs(n)
            actual += abs(n)
        
        return [bad_num, expected-(actual-bad_num)]

test_case1=[1,2,2,4]
s = Solution()
s.findErrorNums(test_case1)
