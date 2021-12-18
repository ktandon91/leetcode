class Solution:
    def subsets(self, nums):
        result = []
        
        if len(nums) == 0:
            return result
        
        def recursive_solution(n, sol):    
            if n==len(nums):
                return result.append(sol[:])
            sol.append(nums[n])
            recursive_solution(n+1, sol)
            sol.pop()
            recursive_solution(n+1, sol)
            
        
        recursive_solution(0,[])
        return result

test_case = [1,2,3]
s = Solution()
print(s.subsets(test_case))
