class Solution:
    def reversed_invert_str(self, s):
        new_s = ""
        for c in s:
            if c == "1":
                new_s+="0"
            else:
                new_s+="1"
        return new_s[::-1]

    def findKthBit2(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        generated_str = "0"
        for i in range(1, n):
            generated_str = generated_str + "1" + self.reversed_invert_str(generated_str)
        print(generated_str)
        return generated_str[k-1]
    
    def findKthBit(self, n, k):
        if n == 1:
            return "0"
        
        h = 1 << (n-1) 

        if k == h:
            return "1"
        
        elif k < h:
            return self.findKthBit(n-1, k)
        else:
            x = 2*h-k
            r = self.findKthBit(n-1,x)
            if r == "1":
                return "0"
            return "1"
s = Solution()
print(s.findKthBit(4,11))