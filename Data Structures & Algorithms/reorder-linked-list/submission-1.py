# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head

        # find half way node
        slow, fast = curr, curr.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        firstHalf = head
        secondHalf = slow.next

        # reverse second half

        prev = slow.next = None
        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = temp

        first, second = head, prev
        
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


            
            



