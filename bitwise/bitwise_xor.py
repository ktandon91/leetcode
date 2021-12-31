# Swap 2 no.s
def swapTwoNumbers():
    a = 10 
    b = 121
    a = a ^ b
    print(a)
    b = b ^ a
    print(b)
    a = a ^ b
    print(a)
# swapTwoNumbers()

# Problem
# Find odd occuring element
# if we take XOR of zero and a bit, it will return that bit.
# a ^ 0 = a
# If we take XOR of duplicate bits, it will return 0.
# a ^ a = 0
# LeetCode problem of finding single occurence of number where there are duplicates

# Problem
# Check if two numbers has opposite sign
# x^y > 0, same sign numbers else opposite sign numbers
a = 10
b = -100
c = 100
print(a^b)
print(a^c)


# Hamming Distance
# How many bits in two numbers are different
def hammingDistance(a, b):
    xor = a ^ b
    distance = 0

    while (xor != 0):
        if (xor % 2 == 1):
            distance += 1
        xor >>= 1;

    return distance
print(hammingDistance(7,2))

## missing number i ^ nums[i]
