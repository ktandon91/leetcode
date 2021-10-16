class Solution:
    def searchRange(self, nums, target):
        start = 0
        end = len(nums) - 1
        result = [-1, -1]
        if not nums:
            return result
        if target < nums[start]:
            return result
        if target > nums[end]:
            return result
        result[0] = self.binary_search(nums, target, True)
        result[1] = self.binary_search(nums, target, False)

        return result

    def binary_search(self, nums, target, is_start_idx):
        start = 0
        end = len(nums) - 1
        temp_ans = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                temp_ans = mid
                if is_start_idx:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return temp_ans