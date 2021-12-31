from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0]
        for i in range(1, num+1):
            ## Based on the premise counter(2N) == counter(N)
            ## Also counter(2N+1) == counter(N) + 1
            counter.append(counter[i >> 1] + i % 2)
        return counter
