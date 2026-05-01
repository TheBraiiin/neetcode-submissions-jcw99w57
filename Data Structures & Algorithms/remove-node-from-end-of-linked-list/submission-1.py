# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        prev.next = self.reverse(head)
        curr = prev.next

        while n - 1> 0:
            prev = prev.next
            curr = curr.next
            n -= 1

        prev.next = curr.next
        curr.next = None
        res = dummy.next
        dummy.next = None

        return self.reverse(res)


        

    def reverse(self, head):
        prev = None

        while head:
            next = head.next
            head.next = prev 
            prev = head
            head = next

        return prev