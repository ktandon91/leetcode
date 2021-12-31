# Find bit length
def find_bit_length(num):
    bit_counter = 0
    while (1 << bit_counter) <= num:
        bit_counter+=1
    return bit_counter

# print(find_bit_length(7))


# Check if kth bit is set
n = 4
k=3
print(1 << k-1)
a = True if (n & (1 << (k - 1))) != 0 else False
print(a)
