class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) != len(b):
            a, b = max(a, b, key=len), min(a, b, key=len)
        i, j = len(a)-1, len(b)-1
        result = []
        carry = 0
        while i>=0 and j >=0:
            d_sum = int(a[i]) + int(b[j]) + carry
            carry = d_sum // 2
            result.append(str(d_sum % 2))
            i-=1
            j-=1
        
        if i>=0:
            while i>=0:
                d_sum = carry + int(a[i])
                result.append(str(d_sum % 2))
                carry = d_sum // 2
                i-=1
        
        if carry and i<0:
            result.append(str(carry))
        
        result = ''.join(reversed(result))
        
        return result

s=Solution()
print(s.addBinary("100","110010"))