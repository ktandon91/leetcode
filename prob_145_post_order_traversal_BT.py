# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None or not root :
            return []
        
        result = []
        
        def post_order(root):
            if root is None:
                return
            post_order(root.left)
            post_order(root.right)
            result.append(root.val)
        post_order(root)
        return result

        