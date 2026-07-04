# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def display(self, node):
        while node:
            print(node.val , '->')
            node = node.next
    def reverseList(self, head):
        prev = None
        curr = head
        size = 0
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            size = size+1
        return prev, size

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, size = self.reverseList(head)
        copy = prev

        dummy = ListNode(0)
        dummy.next = copy

        prev = dummy
        i = 1

        while prev.next and i <= n:
            if i == n:
                prev.next = prev.next.next
                break
            prev = prev.next
            i += 1

        prev, _ = self.reverseList(dummy.next)
        return prev
