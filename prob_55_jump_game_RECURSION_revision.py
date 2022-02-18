from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        c, max_jump = 0, 0 
        for idx, val in enumerate(nums):
            max_jump = max(max_jump, idx+val)
            if c == idx:
                c = max_jump
            if c + 1 >= n:
                return True
        return False
    

test_case = [3,2,1,0,4]
print(Solution().canJump(test_case))
