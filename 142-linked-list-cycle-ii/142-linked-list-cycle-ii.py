# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = self.detectIntersect(head)
        if ptr2 is None:
            return None
        else:
            while ptr1 != ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
        return ptr1
    
    def detectIntersect(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None