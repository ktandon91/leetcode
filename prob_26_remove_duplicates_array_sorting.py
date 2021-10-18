class Solution:
    def removeDuplicates1(self, nums) -> int:
        start = 0
        end = len(nums)-1
        while start < end:
            j = start+1
            if nums[start] == nums[j]:
                nums[j], nums[end] = nums[end], nums[j]
                end -= 1
                while j < end and nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    j += 1
            elif nums[start] != nums[j]:
                start += 1
        return end + 1
    
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        last = 0
        for num in nums:
            if num > nums[last]:
                last+=1
                nums[last] = num
        return last + 1

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))