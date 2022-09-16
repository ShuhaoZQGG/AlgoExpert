# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = head
        target = head
        tail = head
        while n > 0:
            tail = tail.next
            n -= 1
        if tail is None:
            return res.next
        while tail.next:
            target = target.next
            tail = tail.next
        target.next = target.next.next
        return res
