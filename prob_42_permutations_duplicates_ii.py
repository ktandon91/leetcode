from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        def recursive_solution(nums, d):
            result = [] 
            if len(nums) == 1:
                return [nums[:]]
            for key in d:
                if d[key] > 0:
                    nums.remove(key)
                    d[key]-=1
                    perms = recursive_solution(nums, d)
                    for perm in perms:
                        perm.append(key)
                    result.extend(perms)
                    d[key]+=1
                    nums.append(key)
            return result
        return recursive_solution(nums, d)

test_case = [1,2,3]
s = Solution()
print(s.permuteUnique(test_case))
