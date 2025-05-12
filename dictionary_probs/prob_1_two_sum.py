class Solution:
    def twoSum_my_solution(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, n in enumerate(nums):
            if n not in d:
                d[n] = [idx]
            else:
                d[n].append(idx)
        
        for n, idx in d.items():
            second_n = target - n
            if n == second_n:
                if len(d[n]) > 1:
                    return d[n]
            elif second_n in d:
                return [idx[0], d[second_n][0]]
        
    def twoSum(self, nums, target):
        seen = {}
        for idx, n in enumerate(nums):
            second_n = target - n
            if second_n in seen:
                return [seen[second_n], idx]
            else:
                seen[n]=idx
        
