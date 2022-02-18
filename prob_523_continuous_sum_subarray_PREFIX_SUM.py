# Idea: if sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i. Once some later sum(nums[:i']) % k == sum(nums[:i]) % k and i' - i > 1, we return True.

# Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n).

# For example for array [23,4,8] and k = 6 
# we can see for indices 1 and 2 we have a subarray [4,8] which satisfies the constraint
# sum([23,4]) = 27, 27 % 6 = 3
# sum([23,4,6]) = 33 % 6 = 3
# Which implies while iterating over the elements we have to store the mod of the prefix sum and whenever we encounter an existing mod we can return true

from typing import List


class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         prefix_sum = {0:-1}
#         agg = 0
#         for idx, num in enumerate(nums):
#             if k != 0:
#                 agg = (agg + num)%k
#             else:
#                 agg+=num
                
#             if agg in prefix_sum:
#                 if idx - prefix_sum[agg] > 1:
#                     return True
#             else:
#                 prefix_sum[agg] = idx
#         return False
    
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = {0:-1}
        agg = 0
        for idx, num in enumerate(nums):
            agg+=num
            key = agg%k if k!=0 else agg
            if key in prefix_sum:
                if idx - prefix_sum[key] > 1:
                    return True
            else:
                prefix_sum[agg] = idx
        return False

test_case=[23,2,4,6,7]
test_case2=[5,0,0,0]
print(Solution().checkSubarraySum([2,4], 6))
