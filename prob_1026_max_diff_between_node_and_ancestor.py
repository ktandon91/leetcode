# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, min_ancestor, max_ancestor, result):
            if node is None:
                return max_ancestor - min_ancestor
            min_ancestor = min(min_ancestor, node.val)
            max_ancestor = max(max_ancestor, node.val)
            result = max(dfs(node.left, min_ancestor, max_ancestor, result), 
                         dfs(node.right, min_ancestor, max_ancestor, result))
            return result
        return dfs(root, root.val, root.val, 0)      
