# There are three main types of shifts:
# Left shift: << is the left shift operator and meets both logical and arithmetic shifts’ needs.
# Arithmetic/signed right shift: >> is the arithmetic (or signed) right shift operator.
# Logical/unsigned right shift: >>> is the logical (or unsigned) right shift operator.

# 1011 >> 1  →  1101
# 1011 >> 3  →  1111

# 0011 >> 1  →  0001
# 0011 >> 2  →  0000

# The first two numbers had a 1 as the most significant bit, 
# so more 1's were inserted during the shift. 
# The last two numbers had a 0 as the most significant bit, 
# so the shift inserted more 0's.

# If a number is encoded using two’s complement, then an arithmetic 
# right shift preserves the number’s sign, while a logical 
# right shift makes the number positive.
