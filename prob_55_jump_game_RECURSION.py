from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def recursive_solution(c, target, combination):
            n = len(c)

            if target == 0:
                result.append(combination)
                return 
            
            if target < 0:
                return
            
            for i in range(n):
                recursive_solution(c[i:], target-c[i], combination+[c[i]])
                
        recursive_solution(candidates, target, [])
        return result

print(Solution().combinationSum([2,3,6,7], 7))




class Solution:
    def combinationSum(self, candidates, target: int):
        results=[]
        
        def recursive_solution(i, cur, total):     ## 0, [2], 2
            if total == target:
                results.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            
            recursive_solution(i, cur, total+candidates[i])
            cur.pop() #0, [], 0
            recursive_solution(i+1, cur, total)
            
        recursive_solution(0, [], 0)    
        return results
