# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1, t2 = l1, l2
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while t1 or t2:
            res = carry
            if t1:
                res += t1.val
            if t2:
                res += t2.val
            new = ListNode(res % 10)
            curr.next = new
            curr = curr.next
            carry = res // 10
            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
        if carry:
            new = ListNode(carry)
            curr.next = new
        return dummy.next
