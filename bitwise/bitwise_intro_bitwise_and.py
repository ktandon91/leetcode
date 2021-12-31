a = 8

# Bitwise shift left muliplies the number by power of 2**(shift_value)
print(a << 3) # will multiply a with 2**3 

# Bitwwise shift right will divide the number by 2**(shift value)
print(a >> 3) # will divide a by 2**3

# 
print(a & 3) # 


# Brian Kernighan’s algorithm
# is used to count set bits of a number
# Time complexity: O(Set Bit count) / O(1) in simple terms
# Space Complexity: O(1)
a = 8000
count=0
while a > 0:
    a &= (a-1)
    count+=1
print(count)

## Another way to find number of bits for a very large number
## Idea is to maintain a table of result for first 256 numbers 0-255
## Then using this lookup table divide the large number in 4 separate bytes
## Calculate each byte set bits and add them
## Trick is table[n & 0xff] i.e table[n&255] 255 has all 8 bits set
## then shift n by 8 bits to the right n>>=8
n = 8000
table = [0] * 256
for i in range(256):
    table[i] = (i & 1) + table[i >> 1]
res = 0 
for i in range(4): 
    res += table[n & 0xff]
    n >>= 8
print(res)

## Number is a power of 2
n = 8
m = 10
if (n != 0) and (n & n-1) == 0 :
    print(True)
else:
    print(False)
print(True if (m != 0) and (m & m-1) ==0 else False) 

