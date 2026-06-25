# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_arr, l2_arr = [], []
        while list1:
            l1_arr.append(list1.val)
            list1 = list1.next
        while list2:
            l2_arr.append(list2.val)
            list2 = list2.next
        i, j = 0,0
        new_list = None
        curr = None
        while i < len(l1_arr) and j < len(l2_arr):
            new_node = None
            if l1_arr[i] <= l2_arr[j]:
                new_node = ListNode(l1_arr[i])
                i+=1
            else:
                new_node = ListNode(l2_arr[j])
                j+=1
            if not new_list:
                new_list = new_node
                curr = new_list
            else:
                curr.next = new_node
                curr = curr.next
        while i < len(l1_arr):
            print("reached")
            new_node = ListNode(l1_arr[i])
            if not new_list:
                new_list = new_node
                curr = new_list
            else:
                curr.next = new_node
                curr = curr.next
            i+=1
        while j < len(l2_arr):
            print("reached j loop")
            new_node = ListNode(l2_arr[j])
            print(new_node.val)
            if not new_list:
                new_list = new_node
                curr = new_list
            else:
                curr.next = new_node
                curr = curr.next
            j+=1
        return new_list


