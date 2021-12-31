"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = []
        q.append(root)
        nodes_left_in_layer = 1
        nodes_in_next_layer = 0
        layers = []
        result = []
        while q:
            node = q.pop(0)
            result.append(node)    
            
            if node.left is not None:
                q.append(node.left)
                nodes_in_next_layer+=1
            
            if node.right is not None:
                q.append(node.right)
                nodes_in_next_layer+=1
            
            nodes_left_in_layer-=1
            if nodes_left_in_layer == 0:
                nodes_left_in_layer = nodes_in_next_layer
                nodes_in_next_layer = 0
                layers.append(result)
                result = []
                
        for layer in layers:
            n = len(layer)
            for i in range(n):
                if i==n-1:
                    layer[i].next = None
                else:
                    layer[i].next = layer[i+1]
        return root
    
    # Constant Space Copied
    def connect(self, root: 'Node') -> 'Node':
        node = root
        tail = dummy = Node(0)
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next
        return root
