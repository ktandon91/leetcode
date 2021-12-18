class Solution:
    def generateParenthesis(self, n: int):
        results = []
        
        def recursive_solution(opening, closing, temp_str):
            if opening == 0 and closing == 0:
                results.append(temp_str)
                return
            if opening == closing:
                recursive_solution(opening-1, closing, temp_str+"(")
            
            if opening != closing:
                if opening != 0:
                    recursive_solution(opening-1, closing, temp_str+"(")
                    recursive_solution(opening, closing-1, temp_str+")")
                else:
                    recursive_solution(opening, closing-1, temp_str+")")
        
        recursive_solution(n,n,"")
        return results

s = Solution()
print(s.generateParenthesis(3))
