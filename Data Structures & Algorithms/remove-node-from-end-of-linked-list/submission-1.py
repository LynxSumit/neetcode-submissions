# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next
        n = len(nodes)
        for i in range(n-1, -1, -1):
            if i == n-k:
                nodes.pop(i)
                break
        temp = None
        new_head = None
        for node in nodes:
            if not temp:
                temp = node
                new_head = node
            else:
                temp.next = node
                temp = temp.next
        if temp:
            temp.next = None
        return new_head



