from copy import deepcopy

class Solution:
    def unoptimized_combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def recusive_solution(pos, cur, total):
            if total == target:
                result.append(cur[:])
            if pos >= len(candidates) or total > target:
                return

            prev = -1

            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                recusive_solution(i+1, cur, total+candidates[i])
                cur.pop()
                prev = candidates[i]
        
        recusive_solution(0, [], 0)
        return result
    
    def combinationSum2(self, candidates, target):
        candidates_dict = {}
        for candidate in candidates:
            if candidate in candidates_dict:
                candidates_dict[candidate]+=1
            else:
                candidates_dict[candidate]=1
        
        result = []

        def recusive_solution(i, cur, total, candidates_dict):
            if i >= len(candidates) or total > target:
                return
            if total == target:
                result.append(cur[:])
                return True
            if candidates_dict[candidates[i]] == 0:
                return
            
            cur.append(candidates[i])
            candidates_dict[candidates[i]]-=1
            r = recusive_solution(i+1, cur, total+candidates[i], candidates_dict)
            if not r:
                cur.pop()
            else:
                cur = []
            # candidates_dict[candidates[i]]+=1
            recusive_solution(i+1, cur, total, candidates_dict)
            
        recusive_solution(0, [], 0, candidates_dict)
        return result
    
s = Solution()
# print(s.combinationSum2([10,1,2,7,6,1,5], 8))
# print(s.combinationSum2([1,1,1], 2))
print(s.unoptimized_combinationSum2([1,1,1], 2))