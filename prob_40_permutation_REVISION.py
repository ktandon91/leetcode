from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def recursive_solution(nums, temp_result):
            if len(temp_result) == n:
                result.append(temp_result)
            for i in range(len(nums)):
                element = nums.pop(0)
                recursive_solution(nums, temp_result + [element])
                nums.append(element)
        recursive_solution(nums, [])
        return result
test_case = [1,1,2]
s = Solution()
print(s.permute(test_case))
