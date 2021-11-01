class Solution:
    def addToArrayForm(self, nums, k: int):
        i = len(nums) - 1
        carry = k
        while i >=0 :
            digits_sum = carry + nums[i]
            digit = digits_sum % 10
            carry = digits_sum // 10
            nums[i] = digit
            if carry == 0:
                break
            i-=1
        
        if carry:
            nums2 = []
            while carry:
                nums2.append(carry%10)
                carry = carry // 10
            
            nums2 = list(reversed(nums2))
            nums = nums2 + nums    

        return nums

s = Solution()
print(s.addToArrayForm([6], 809))