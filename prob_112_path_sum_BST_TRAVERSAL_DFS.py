# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def recursive_solution(root, running_sum, left_result, right_result):
            if root is None:
                return False
            
            if root.left is None and root.right is None:
                running_sum = running_sum + root.val
                if running_sum  == targetSum:
                    return True
                return False
            
            if root.left is not None:
                left_result = recursive_solution(root.left, running_sum+root.val, left_result, right_result)
            
            if root.right is not None:
                right_result = recursive_solution(root.right, running_sum+root.val, left_result, right_result)
            
    
            if left_result or right_result:
                return True
            
            return False
        
        return recursive_solution(root, 0, False, False)
