# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        prevGroup = dummy
        nextGroup = head

        while curr:
            r = curr
            i = 0
            while r and i < k:
                r = r.next
                i += 1

            if i < k:
                break


            prev = r
            
            i = 0
            while curr and i < k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                i += 1
            
            prevGroup.next = prev
            prevGroup = nextGroup
            nextGroup = curr

        return dummy.next


        # dummy 3 -> 2 -> 1 -> 4 -> 5 -> 6
        # pg    c       ngpr   t


        