from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_time=releaseTimes[0]
        key = keysPressed[0]
        for i in range(1, len(releaseTimes)-1):
            if (releaseTimes[i] - releaseTimes[i-1]) > max_time:
                max_time = releaseTimes[i] - releaseTimes[i-1]
                key = keysPressed[i]
            elif (releaseTimes[i] - releaseTimes[i-1]) == max_time:
                key = max(key, keysPressed[i])
        return key

s = Solution()
release = [12,23,36,46,62]
keys = "spuda"
s.slowestKey(release, keys)
