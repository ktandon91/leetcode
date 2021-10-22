# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None or not root :
            return []
        
        result = []
        
        def in_order(root):
            if root is None:
                return
            in_order(root.left)
            result.append(root.val)
            in_order(root.right)
        
        in_order(root)
        return result
                