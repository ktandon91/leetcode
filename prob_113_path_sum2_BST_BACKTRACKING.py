# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def recursive_solution(root, running_sum, nodes_in_sum):
            if root is None:
                return result
            
            nodes_in_sum.append(root.val)

            if root.left is None and root.right is None:
                if (running_sum + root.val) == targetSum:
                    result.append(nodes_in_sum[:])
            
            if root.left is not None:
                recursive_solution(root.left, running_sum+root.val, nodes_in_sum)
            
            if root.right is not None:
                recursive_solution(root.right, running_sum+root.val, nodes_in_sum)
            
            nodes_in_sum.pop()
        
        recursive_solution(root, 0, [])
        return result
    
            