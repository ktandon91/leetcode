# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None or not root :
            return []
        
        result = []
        
        def pre_order(root):
            if root is None:
                return
            result.append(root.val)
            pre_order(root.left)
            pre_order(root.right)
        
        pre_order(root)
        return result

        