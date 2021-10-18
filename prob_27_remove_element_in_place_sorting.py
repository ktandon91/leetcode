class Solution:
    def removeElement(self, nums, val: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1 and val == nums[0]:
            return 0
        start = 0
        last = len(nums) - 1
        while start <= last:
            if nums[start] == val:
                while last > -1 and nums[last] == val:
                    last-=1
                if last > start:
                    nums[start], nums[last] = nums[last], nums[start]
                    last -= 1
            start+=1
        return last + 1

if __name__ == "__main__":
    s = Solution()
    print(s.removeElement([4, 5], 5))