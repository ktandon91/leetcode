class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0]+nums[2], nums[1])
        max_arr = [-1 for _ in range(n)]
        def rs(i):
            if max_arr[i] != -1:
                return max_arr[i]
            if i >= n:
                return 0
            if i == n-1:
                return nums[i]
            else:
                l = nums[i]+rs(i+2)
                r = nums[i+1]+rs(i+3)
                max_arr[i] = max(l, r)
                return max_arr[i]
        return rs(0)

test_case1 = [1,2,3,1]
s = Solution()
print(s.rob(test_case1))
