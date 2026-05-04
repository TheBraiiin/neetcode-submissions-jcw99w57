# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = head
        prev = dummy

        while n > 0:
            fast = fast.next
            n -= 1

        while fast:
            prev = prev.next
            fast = fast.next
        
        prev.next = prev.next.next

        return dummy.next

