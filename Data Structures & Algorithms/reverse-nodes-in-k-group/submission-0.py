# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = r = head
        i = 0  

        while r and i < k:
            r = r.next
            i += 1

        if i < k:
            return head

        prev = None
        while curr != r:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1
        
        newHead = prev
        prevTail = head
        prevTail.next = curr

        while curr:
            r = curr
            i = 0

            while r and i < k:
                r = r.next
                i += 1

            if i < k:
                break

            groupTail = curr
            prev = None

            while curr != r:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            prevTail.next = prev

            groupTail.next = curr

            prevTail = groupTail

        return newHead
