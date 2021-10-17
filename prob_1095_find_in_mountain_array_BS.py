# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        start = 0
        end = mountain_arr.length() - 1
        peak_element = float('-inf')
        peak_idx = -1
        last_element = mountain_arr.get(end)
        first_element = mountain_arr.get(start)

        if target < first_element and target < last_element:
            return -1

        while start <= end:
            mid = (start + end) // 2
            middle = mountain_arr.get(mid)
            right_to_middle = mountain_arr.get(mid + 1)

            if middle < right_to_middle:
                start = mid + 1
            else:
                if peak_element < middle:
                    peak_element = middle
                    peak_idx = mid
                end = mid - 1
        peak_element = mountain_arr.get(peak_idx)
        print(f"peak element = {peak_element}")
        if target > peak_element:
            return -1

        def binary_search(mountain_arr, target, peak_idx, ascending):
            ans = None
            if ascending:
                start = 0
                end = peak_idx
            else:
                start = peak_idx + 1
                end = mountain_arr.length() - 1

            while start <= end:
                mid = (start + end) // 2
                element = mountain_arr.get(mid)
                if element == target:
                    if not ans:
                        ans = mid
                    else:
                        ans = min(ans, mid)
                    end = end - 1
                elif element > target:
                    if ascending:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if ascending:
                        start = mid + 1
                    else:
                        end = mid - 1
            return ans

        left_of_peak = binary_search(mountain_arr, target, peak_idx, ascending=True)
        print(f"lef of peak element = {left_of_peak}")
        if left_of_peak is None:
            right_of_peak = binary_search(mountain_arr, target, peak_idx, ascending=False)
        else:
            return left_of_peak
        if right_of_peak is not None:
            return right_of_peak
        else:
            return -1
