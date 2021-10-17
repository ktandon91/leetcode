class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        if len(nums) == 1:
            if nums[0] != target:
                return -1
            else:
                return 0

        def get_peak_index(nums):
            start = 0
            end = len(nums) - 1
            ans = -1
            while start <= end:
                mid = (start + end) // 2
                if mid < end and nums[mid] > nums[mid + 1]:
                    ans = mid
                    break
                if mid > start and nums[mid] < nums[mid - 1]:
                    ans = mid - 1

                if nums[start] > nums[mid]:
                    end = mid - 1
                elif nums[start] <= nums[mid]:
                    start = mid + 1
            return ans

        def binary_search(mountain_arr, target, start, end):
            ans = None
            while start <= end:
                mid = (start + end) // 2
                element = mountain_arr[mid]
                if element == target:
                    if not ans:
                        ans = mid
                    else:
                        ans = min(ans, mid)
                    end = end - 1
                elif element > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return ans

        peak_idx = get_peak_index(nums)

        if peak_idx == -1:
            peak_idx = len(nums) - 1
        left_result = binary_search(nums, target, 0, peak_idx)

        if peak_idx == len(nums) - 1 and left_result is None:
            return -1

        if left_result is not None:
            return left_result
        else:
            right_result = binary_search(nums, target, peak_idx + 1, len(nums) - 1)

        if right_result is not None:
            return right_result
        else:
            return -1
        return result