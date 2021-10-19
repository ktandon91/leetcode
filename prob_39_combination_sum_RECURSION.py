from copy import deepcopy
from typing import List

class Solution:
    def combinationSum(self, candidates, target: int):
        results=[]
        
        def recursive_solution(i, cur, total):    
            if total == target:
                results.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            
            recursive_solution(i, cur, total+candidates[i])
            cur.pop()
            recursive_solution(i+1, cur, total)
            
        recursive_solution(0, [], 0)    
        return results
    
    

s = Solution()
print(s.combinationSum([1,2,3],3))