# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         if len(a) != len(b):
#             a, b = max(a, b, key=len), min(a, b, key=len)
#         i, j = len(a)-1, len(b)-1
#         result = []
#         carry = 0
#         while i>=0 and j >=0:
#             d_sum = int(a[i]) + int(b[j]) + carry
#             carry = d_sum // 2
#             result.append(str(d_sum % 2))
#             i-=1
#             j-=1
        
#         if i>=0:
#             while i>=0:
#                 d_sum = carry + int(a[i])
#                 result.append(str(d_sum % 2))
#                 carry = d_sum // 2
#                 i-=1
        
#         if carry and i<0:
#             result.append(str(carry))
        
#         result = ''.join(reversed(result))
        
#         return result

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a)-1
        n = len(b)-1
        a = list(a)
        b = list(b)
        carry = 0
        if m < n:
            a, b = b, a
            m, n = n, m
        while m >= 0:
            digit_a = int(a[m])
            if n < 0:
                digit_b = 0
            else:
                digit_b = int(b[n])
            if digit_a + digit_b + carry > 1:
                digit = (digit_a + digit_b + carry) % 2
                carry = (digit_a + digit_b + carry) // 2
            else:
                digit = digit_a + digit_b + carry
                carry = 0
            a[m] = str(digit)
            m-=1
            n-=1
        if carry:
            a = [str(carry)] + a
        return "".join(a)

s=Solution()
print(s.addBinary("1","111"))
