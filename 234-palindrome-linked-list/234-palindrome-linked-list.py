# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        fast = self.reverseLL(slow.next)
        while fast:
            if head.val != fast.val:
                return False
            head = head.next
            fast = fast.next
        return True
        
    def reverseLL(self, head):
        prev, curr = None, head
        while curr:
            nextCurr = curr.next
            curr.next = prev
            prev = curr
            curr = nextCurr
        return prev