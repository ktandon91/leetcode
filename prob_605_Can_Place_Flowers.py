
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = len(flowerbed)
        i = 0
        while i < f and n > 0:
            if flowerbed[i] == 0:
                left_empty = True if (i == 0 or flowerbed[i-1]==0) else False 
                right_empty = True if (i==f-1 or flowerbed[i+1]==0) else False
                if left_empty and right_empty:
                    flowerbed[i]=1
                    n-=1
            i+=1    
        if n > 0:
            return False
        return True
