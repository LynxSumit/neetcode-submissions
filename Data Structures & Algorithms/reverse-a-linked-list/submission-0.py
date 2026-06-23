# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        new_head = None 
        temp = None
        print(arr)
        for val in reversed(arr):
            # print(val)
            if new_head == None:
                temp = ListNode(val, None)
                new_head = temp
            else:
                temp.next = ListNode(val, None)
                temp = temp.next
        return new_head
