from typing import Sequence


class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        sq_of_digits = 0
        d = {}
        d[num] = "encountered"
        while num != 0:
            digit = num % 10
            num = num // 10
            sq_of_digits = sq_of_digits + digit*digit
           
            if num == 0 and sq_of_digits == 1:
                return True
            elif num == 0:
                if sq_of_digits in d:
                    return False
                else:
                    d[sq_of_digits] = "encountered"
                num = sq_of_digits
                sq_of_digits = 0
            
        return happy_number