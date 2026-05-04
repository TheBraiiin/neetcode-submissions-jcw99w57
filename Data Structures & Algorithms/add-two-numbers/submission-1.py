# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 and l2:
            curr_val = l1.val + l2.val + carry

            if curr_val > 9:
                carry = 1
                curr_val -= 10
            else:
                carry = 0    

            curr.next = ListNode(curr_val)
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        rlist = l1 or l2

        while rlist:
            curr_val = rlist.val + carry
            if curr_val > 9:
                carry = 1
                curr_val -= 10
            else:
                carry = 0    

            curr.next = ListNode(curr_val)
            curr = curr.next

            rlist = rlist.next

        if carry == 1:
            curr.next = ListNode(carry)
        

        return dummy.next

            