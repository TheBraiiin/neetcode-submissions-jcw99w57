# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        mid = self.reverse(mid)

        while mid:
            head_next = head.next
            mid_next = mid.next

            head.next = mid
            mid.next = head_next

            head = head_next
            mid = mid_next

            # 2, 4, 6
            # 10, 8

            # 2
        

    def reverse(self, head):
        prev = None

        while head:
            next = head.next
            head.next = prev 
            prev = head
            head = next

        return prev