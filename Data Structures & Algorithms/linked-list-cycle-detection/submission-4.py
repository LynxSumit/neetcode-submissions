# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fst = head
        snd = head.next if head else None
        while fst and snd:
            if fst.val == snd.val:
                return True
            fst = fst.next
            snd = snd.next.next if snd.next else snd.next
        return False

