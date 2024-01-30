from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])
        
        top = 0
        bottom = height - 1
        left = 0
        right = width - 1
        
        ans = []
        while top < bottom and left < right:
            for c in range(left, right):
                ans.append(matrix[top][c])
            
            for r in range(top, bottom):
                ans.append(matrix[r][right])
            
            for c in range(right, left, -1):
                ans.append(matrix[bottom][c])
            
            for r in range(bottom, top, -1):
                ans.append(matrix[r][left])

            top+=1
            bottom-=1
            right-=1
            left+=1

        if left == right and top == bottom:
            ans.append(matrix[left][left])
        elif left == right:
            for r in range(top, bottom+1):
                ans.append(matrix[r][left])
        elif top == bottom:
            for c in range(left, right+1):
                ans.append(matrix[top][c])
        
        return ans


test_case = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
print(s.spiralOrder(test_case))
