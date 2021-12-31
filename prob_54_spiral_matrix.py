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
            for col in range(left, right):
                ans.append(matrix[top][col])
            
            for row in range(top, bottom):
                ans.append(matrix[row][right])
            
            for col in range(right, left, -1):
                ans.append(matrix[bottom][col])
            
            for row in range(bottom, top, -1):
                ans.append(matrix[row][left])
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1
            
        return ans
    
    def spiralOrderCopy(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res
        row_begin = 0
        col_begin = 0
        row_end = len(matrix)-1 
        col_end = len(matrix[0])-1
        while (row_begin <= row_end and col_begin <= col_end):
            for i in range(col_begin,col_end+1):
                res.append(matrix[row_begin][i])
            row_begin += 1
            for i in range(row_begin,row_end+1):
                res.append(matrix[i][col_end])
            col_end -= 1
            if (row_begin <= row_end):
                for i in range(col_end,col_begin-1,-1):
                    res.append(matrix[row_end][i])
                row_end -= 1
            if (col_begin <= col_end):
                for i in range(row_end,row_begin-1,-1):
                    res.append(matrix[i][col_begin])
                col_begin += 1
        return res


test_case = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
test_case2 = [[1,2,3]]
test_case3 = [[1,2,3],[4,5,6],[7,8,9]]
test_case4 = [[7],[9],[6]]
print(Solution().spiralOrder(test_case2))
