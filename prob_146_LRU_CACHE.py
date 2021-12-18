class ListNode:
    def __init__(self, key,val, left=None, right=None):
        self.key=key
        self.val=val
        self.left=left
        self.right=right

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_tail(self, node):
        if self.head is None:
            self.head, self.tail = node, node
        else:
            node.left = self.tail
            self.tail.right = node
            self.tail = self.tail.right
    
    def delete_from_head(self):
        node_to_delete = self.head
        if self.head.right is not None:
            self.head = self.head.right
            self.head.left = None
        else:
            self.head, self.tail = None, None
        del node_to_delete
    
    def delete_node(self, node):
        if node.right is not None:
            if node.left is None:
                self.head = self.head.right
                self.head.left = None
            else:
                node.left.right = node.right
                node.right.left = node.left
        elif node.left is None and node.right is None:
            self.head, self.tail = None, None 
        else:
            self.tail = self.tail.left
            self.tail.right = None
        del node
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.cache_values = LinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            address = self.cache[key]
            value = address.val
            # if address.right is None:
            #     return value
            self.put(key, address.val)
        else:
            value = -1
        # print(f"Cache State while return key {key}")
        # ptr = self.cache_values.head
        # while ptr is not None:
        #     print(ptr.val)
        #     ptr = ptr.right
        return value

    def put(self, key: int, value: int) -> None:
        new_node = ListNode(key, value)
        if key not in self.cache:
            if self.capacity > 0:
                self.cache_values.insert_at_tail(new_node)
                self.capacity-=1
            else:
                del self.cache[self.cache_values.head.key]
                self.cache_values.delete_from_head()
                self.cache_values.insert_at_tail(new_node)
        else:
            node = self.cache[key]
            self.cache_values.delete_node(node)
            self.cache_values.insert_at_tail(new_node)
        self.cache[key] = new_node


# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
lru = LRUCache(3)
# lru.put(2,1)
# lru.put(2,2)
# lru.get(2)
# lru.put(1,1)
# lru.put(4,1)
# lru.get(2)
["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
[[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]

lru.put(1,1)
lru.put(2,2)
lru.put(3,3)
lru.put(4,4)
lru.get(4)
lru.get(3)
lru.get(2)
lru.get(1)
lru.put(5,5)
lru.get(1)
lru.get(2)
lru.get(3)
lru.get(4)
lru.get(5)
