# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate_tree(node, left_value, right_value):
            if node is None:
                return True
            if not (left_value < node.val) or not (right_value > node.val):
                return False
            return validate_tree(node.left, left_value, node.val) and validate_tree(node.right, node.val, right_value)
        
        return validate_tree(root, float('-inf'), float('inf'))