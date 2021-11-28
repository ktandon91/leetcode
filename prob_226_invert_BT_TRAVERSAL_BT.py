# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert_tree(node):
            if node is None:
                return
            node.left, node.right = node.right, node.left
            invert_tree(node.left)
            invert_tree(node.right)
            
        invert_tree(root)
        return root
            