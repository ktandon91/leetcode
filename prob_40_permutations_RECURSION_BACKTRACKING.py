class Solution:
    def permute(self, nums):
        result = []
        
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            element = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(element)
            result.extend(perms)
            nums.append(element) 
        return result

s = Solution()
print(s.permute([1,2,3]))
