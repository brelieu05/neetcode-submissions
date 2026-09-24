# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        groupPrev = dummy = ListNode(0, head)

        while True:
            kth = groupPrev

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next
            
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            newTail = groupPrev.next
            groupPrev.next = kth
            groupPrev = newTail

        return dummy.next


        # dummy 3 -> 2 -> 1 -> 4 -> 5 -> 6
        # pg    c       ngpr   t


        