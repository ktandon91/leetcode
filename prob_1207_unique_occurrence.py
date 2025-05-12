from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for e in arr:
            if e not in map:
                map[e] = 0
            map[e]+=1
        s = set()
        for e, occurrence in map.items():
            if occurrence in s:
                return False
            s.add(occurrence)
        return True

s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))