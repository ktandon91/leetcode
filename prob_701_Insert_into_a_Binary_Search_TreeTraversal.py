# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def solve(node, val):
            if node is None:
                return TreeNode(val)
            if node.val > val:
                node.left = solve(node.left, val)
            else:
                node.right = solve(node.right, val)
            return node
        return solve(root, val)
