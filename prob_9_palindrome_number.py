############ Learnings
## in python quotient is derived by //
## division by / will give floating point value
## we will reach mid of the number when reversed_num becomes greater than num

def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_num = 0
    while reversed_num < x:
        reversed_num = reversed_num * 10 + x % 10
        x = x // 10

    return x == reversed_num or x == reversed_num // 10

print(isPalindrome(11))