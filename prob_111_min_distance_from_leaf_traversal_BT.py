# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def minimun_leaf_distance(node, d):
            if node is None:
                return float('inf')
            if node.left is None and node.right is None:
                return d
            result = min(minimun_leaf_distance(node.left, d+1), minimun_leaf_distance(node.right, d+1))
            return result
        result = minimun_leaf_distance(root, 1)
        return result
                