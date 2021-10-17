class Solution:
    def fourSum(self, nums, target: int):
        if len(nums) < 4:
            return []
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            for j in reversed(range(len(nums))):
                if i > j:
                    break
                if nums[i] != nums[j]:
                    k = i + 1
                    l = j - 1

                    while k < l:
                        if nums[i] == nums[k]:
                            k += 1
                        elif nums[j] == nums[l]:
                            l -= 1
                        else:
                            temp_sum = nums[i] + nums[j] + nums[k] + nums[l]
                            if temp_sum == target:
                                result.append((nums[i], nums[j], nums[k], nums[l]))
                                k += 1
                                j -= 1
                            elif temp_sum > target:
                                j -= 1
                            elif temp_sum < target:
                                k += 1
        return list(result)



s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))

