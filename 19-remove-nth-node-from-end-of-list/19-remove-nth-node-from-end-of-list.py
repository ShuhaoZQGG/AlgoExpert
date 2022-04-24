# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseList(head):
            prev, curr = None, head
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev
        
        reverse = reverseList(head)
        dummy = ListNode(0)
        dummy.next = reverse
        curr = dummy
        while curr:
            if n == 1:
                curr.next = curr.next.next
            curr = curr.next
            n -= 1

        return reverseList(dummy.next)