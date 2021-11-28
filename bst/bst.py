class BSTNode:
    def __init__(self, data) -> None:
        self.val = data
        self.left = None
        self.right = None

head = BSTNode(5)

def minimum_value(bst_node):
    current_node = bst_node
    while current_node.left is not None:
        current_node = current_node.left
    return current_node

def delete_node(root, node_value):
    if root is None:
        return root
    if node_value < root.val:
        root.left = delete_node(root.left, node_value)
    elif node_value > root.val:
        root.right = delete_node(root.right, node_value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minimum_value(root.right)
        root.val = temp
        root.right = delete_node(root.right, temp.val)

    return root
    
        
        

        