from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[ 0 for i in range(n)] for i in range(n)]
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        counter = 1
        while top < bottom and left < right:
            for col in range(left, right):
                matrix[top][col]=counter
                counter+=1
            
            for row in range(top, bottom):
                matrix[row][right]=counter
                counter+=1
            
            for col in range(right, left, -1):
                matrix[bottom][col]=counter
                counter+=1
                
            for row in range(bottom, top, -1):
                matrix[row][left]=counter
                counter+=1
                
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        if top==bottom and left == right:
            matrix[left][left]=counter
        elif left == right and top < bottom: # n X 1 matrix
            for i in range(top, bottom+1, 1):
                matrix[i][left]=counter
                counter+=1
        elif top == bottom and left < right: ## 1 X n matrix
            for i in range(left, right+1):
                matrix[top][i] = counter
                counter+=1
            
        return matrix
