# Positive numbers in a programming language is stored as normal binary number.
# Negative numbers are stored as 2's complement.
# If we were given a negative number “-x”, 
# its 2’s complement representation is 2**32 - x

a = 8
b = -8
a_binary = bin(a)
b_binary = bin(b)
print(type(a))
print(type(b))
print(a_binary)
print(b_binary)
print(int(a_binary,2))

a = 10
a_complement = ~a
a_2_completement = a_complement + 1
print(a)
print(a_complement)
print(a_2_completement)
