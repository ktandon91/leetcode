class Solution:
    def plusOne(self, digits):
        l = len(digits) - 1

        while l >=0:
            digit_sum = digits[l] + 1
            carry = digit_sum // 10
            digits[l] = digit_sum % 10
            if carry == 0:
                break
            else:
                l-=1
            
        if carry:
            digits.insert(0, carry)
        
        return digits

s = Solution()
print(s.plusOne([9,9,9]))
                
