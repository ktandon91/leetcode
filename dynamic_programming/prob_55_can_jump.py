from typing import List
class Solution:
    def my_canJump_initial_solution(self, nums: List[int]) -> bool:
        if not nums:
            return True
        n = len(nums)
        if n == 1:
            return True
        can_reach = [False for _ in range(n)]
        can_reach[n-1] = True
        left = n-2
        while left >=0:
            if nums[left] + left >= n-1:
                can_reach[left] = True
            else:
                for i in range(1, nums[left]+1):
                    if can_reach[left+i]:
                        can_reach[left] = True
                        break
            left-=1
        return can_reach[0]
test_case = [2,3,1,0,4]
test_case_2 = [3,2,1,0,4]
test_case_3 = [1,2,3]
s = Solution()
print(s.canJump(test_case_3))
