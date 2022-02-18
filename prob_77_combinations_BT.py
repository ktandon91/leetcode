class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def recursive_solution(i, temp_res):
            if len(temp_res) == k:
                result.append(temp_res[:])
                return
            
            if i > n:
                return
            
            temp_res.append(i)
            recursive_solution(i+1, temp_res)
            temp_res.pop()
            recursive_solution(i+1, temp_res)
        recursive_solution(1, [])
        return result
            