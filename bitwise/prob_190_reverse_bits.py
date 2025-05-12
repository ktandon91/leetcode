class Solution:
    def reverseBits(self, n: int) -> int:
        new_num=0
        for i in range(32):
            lst_bit = (n >> i) & 1
            if lst_bit > 0:
                new_num = 2**(31-i) + new_num
        return new_num
s = Solution()

print(s.reverseBits(2))