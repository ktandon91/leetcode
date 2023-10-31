# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements1(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        curr = head
        prev = None
        while curr is not None:
            if curr.val == val:
                t = curr
                curr = curr.next
                if prev is not None:
                    prev.next = curr
                else:
                    head = head.next
                del t
            else:
                prev = curr
                curr = curr.next
        return head
                
    def removeElements(self, head, val):
        if head is None:
            return head

        dummy_head = ListNode()
        dummy_head.next = head
        curr = head
        prev = dummy_head
        while curr is not None:
            if curr.val == val:
                t = curr
                curr = curr.next
                prev.next = curr
                del t
            else:
                prev = curr
                curr = curr.next
        return dummy_head.next 

        