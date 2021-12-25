from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums_set = set(nums)
        for num in nums_set:
            if num-1 not in nums_set:
                current_num = num
                current_streak = 1
                
                while current_num+1 in nums_set:
                    current_streak+=1
                    current_num = current_num+1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak

s = Solution()
test_case = [100,4,200,1,3,2]
print(s.longestConsecutive(test_case))
