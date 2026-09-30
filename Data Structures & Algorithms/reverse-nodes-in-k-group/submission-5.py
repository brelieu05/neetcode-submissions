# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node

        dummy = ListNode(0, head)

        prevGroup, nextGroup = dummy, head
        curr = head

        while True:
            kth = getKth(prevGroup, k)

            if not kth:
                return dummy.next

            nextGroup = kth.next

            # reverse
            prev, curr = kth.next, prevGroup.next
            while curr != nextGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp
        return dummy.next

            
            