# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        ptr1 = head
        while ptr1 is not None:
            counter+=1
            ptr1 = ptr1.next
        
        ptr1=head
        node_to_delete = counter-n+1
        
        if node_to_delete == 1:
            head = head.next
            return head
        
        i=0
        prev = None
        while i != node_to_delete - 1:
            prev = ptr1
            ptr1 = ptr1.next
            i+=1
        prev.next = ptr1.next
        del ptr1
        return head
        