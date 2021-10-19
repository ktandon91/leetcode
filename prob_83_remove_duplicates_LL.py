# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        ptr1 = head
        ptr2 = head.next
        
        while ptr2 is not None:
            if ptr1.val == ptr2.val:
                t = ptr2.next
                ptr1.next = t
                ptr2 = t
            else:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
        
        return head
                