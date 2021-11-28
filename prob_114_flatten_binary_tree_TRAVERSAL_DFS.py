# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        head = None
        def pre_order(node, head):
            if node is None:
                return node
            
            if head is None:
                head = node
                head.left, head.right = None, None
                ll = head
            
            new_node = TreeNode(node.val)
            ll.right = new_node
            ll = ll.right
            
            pre_order(node.left)
            pre_order(node.right)
        
        pre_order(root, head)
        return head