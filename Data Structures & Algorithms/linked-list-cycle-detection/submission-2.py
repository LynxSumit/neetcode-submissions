# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        res = {}
        dummy = head
        if not dummy:
            return False
        while dummy.next != None:
            if (dummy, dummy.val) in res:
                return True
            res[(dummy, dummy.val)] = True
            dummy = dummy.next
        return False