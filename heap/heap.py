
# Initializing heap - Time Complexity O(1)
# Space Complexity - O(n)

class Heap:
    def __init__(self, size):
        self.custom_list = (size+1)*[None]
        self.max_size = size+1
        self.heap_size = 0


## heapify time complexity 
## T(n) = T(n/2) + T(c) => T(n/2) => O(logn)
## Space complexity will be O(logn) since we will be calling the fuction recursively logn times
def heapify_insert(root, idx, heap_type):
    if idx <= 1:       ######### O(1)
        return         ######## O(1)
    parent_idx = idx//2 ######### O(1)
    if heap_type == "min": ######## O (1)
        if root[idx] < root[parent_idx]: ######## O(1)
            root[idx], root[parent_idx] = root[parent_idx], root[idx] ###### O(1)
            heapify_insert(root, parent_idx, heap_type) ###### O(n/2)
    elif heap_type == "max":    ### either this block will run or above one so time complexity will just contain this
        if root[idx] > root[parent_idx]:
            root[idx], root[parent_idx] = root[parent_idx], root[idx]
            heapify_insert(root, parent_idx, heap_type)
    return root

def heapify_delete(root, idx, heap_type):
    left_child = 2*idx+1
    right_child = 2*idx+1
    swap_child = -1
    
    # Check if root has no children
    if root.heap_size < left_child:
        return

    # Check for one child
    elif root.heap_size == left_child:
        if heap_type == "min":
            if (root.custom_list[idx] > root.custom_list[left_child]):
                root.custom_list[idx], root.custom_list[left_child] = root.custom_list[left_child], root.custom_list[idx]
                return
        if heap_type == "max":
            if (root.custom_list[idx] < root.custom_list[left_child]):
                root.custom_list[idx], root.custom_list[left_child] = root.custom_list[left_child], root.custom_list[idx]
                return
    
    # Check for both children
    else:
        if heap_type == "min":
            if (root.custom_list[left_child] < root.custom_list[right_child]):
                swap_child = left_child
            else:
                swap_child = right_child
             
        if root.custom_list[idx] > root.custom_list[swap_child]:
                root.custom_list[idx], root.custom_list[swap_child] = root.custom_list[swap_child], root.custom_list[idx]
                heapify_delete(root, swap_child, heap_type)
        
        if heap_type == "max":
            if (root.custom_list[left_child] > root.custom_list[right_child]):
                swap_child = left_child
            else:
                swap_child = right_child
             
        if root.custom_list[idx] < root.custom_list[swap_child]:
                root.custom_list[idx], root.custom_list[swap_child] = root.custom_list[swap_child], root.custom_list[idx]
                heapify_delete(root, swap_child, heap_type)
    return root


## Space and Time Complexity O(logn)
def extract_node(root, heap_type):
    if root.heap_size == 0:
        return "No nodes to extract, heap is empty"
    extracted_node = root.custom_list[1]
    # Swap first and last element in heap
    root.custom_list[1], root.custom_list[root.heap_size+1] = root.custom_list[root.heap_size+1], None
    root.heap_size-=1
    heapify_delete(root, 1, heap_type) 
    return extracted_node


## Space complexity O(logn) due to heapify operation
## Space complexity O(logn) due to heapify operation
def insert_node(root, node_value, heap_type):
    if root.heap_size+1 == root.max_size:
        return "Heap if full"
    root.custom_list[root.heap_size+1] = node_value
    root.heap_size+=1
    heapify_insert(root, root.heap_size, heap_type)



# Space Complexity = O(1)
# Time Complexity = O(1)
def peek(root):
    if not root:
        return None
    return root.custom_list[1]

# Space Complexity = O(1)
# Time Complexity = O(1)
def size_of_heap(root):
    if not root:
        return 
    return root.heap_size

binary_heap = Heap(5)

print(size_of_heap(binary_heap))

