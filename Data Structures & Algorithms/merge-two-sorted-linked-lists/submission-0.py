# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2

        dummy = res = ListNode()

        while p1 and p2:
            if p1.val < p2.val:
                res.next = p1
                p1 = p1.next
            else:
                res.next = p2
                p2 = p2.next

            res = res.next
        
        while p1:
            res.next = p1
            p1 = p1.next
            res = res.next

        while p2:
            res.next = p2
            p2 = p2.next
            res = res.next

        return dummy.next