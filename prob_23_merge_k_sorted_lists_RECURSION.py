# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        def merge_lists(l1, l2):
            # print(f"l1 = {l1}")
            # print(f"l2 = {l2}")
            new_head = ListNode()
            new_pointer = new_head
            
            while (l1 is not None) and (l2 is not None):
                if l1.val > l2.val:
                    temp = ListNode(l2.val)
                    l2 = l2.next
                else:
                    temp = ListNode(l1.val)
                    l1 = l1.next
                new_pointer.next = temp
                new_pointer = new_pointer.next
                
            if (l1 is None) and (l2 is not None):
                new_pointer.next = l2
                
            if (l2 is None) and (l1 is not None):
                new_pointer.next = l1
            
            return new_head.next
                    
         
        def recursive_solution(n):
            if n==0:
                return ListNode("")
            if n==1:
                return lists[0]
            if n==2:
                # print("n==2")
                result = merge_lists(lists[0], lists[1])
                # print(f"n==2 result = {result}")
                return result
            
            temp_merged = recursive_solution(n-1)
            merged=merge_lists(temp_merged, lists[n-1])
            return merged
    
        result = recursive_solution(len(lists))
        return result

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_lists(l1, l2):
            # print(f"l1 = {l1}")
            # print(f"l2 = {l2}")
            new_head = ListNode()
            new_pointer = new_head
            
            while (l1 is not None) and (l2 is not None):
                if l1.val > l2.val:
                    temp = ListNode(l2.val)
                    l2 = l2.next
                else:
                    temp = ListNode(l1.val)
                    l1 = l1.next
                new_pointer.next = temp
                new_pointer = new_pointer.next
                
            if (l1 is None) and (l2 is not None):
                new_pointer.next = l2
                
            if (l2 is None) and (l1 is not None):
                new_pointer.next = l1
            
            return new_head.next
        
        n = len(lists)
        
        if n == 0:
            return ListNode("")
        if n == 1:
            return lists[0]
        result = lists[0]
        for i in range(1,n):
            result = merge_lists(result, lists[i])
       
        return result
