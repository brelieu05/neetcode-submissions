"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = tail = Node(0)
        curr = head
        oldToCopy = {None : None}

        while curr:
            oldToCopy[curr] = Node(curr.val)
            tail.next = oldToCopy[curr]
            curr = curr.next
            tail = tail.next

        curr = head
        tail = dummy.next
        while curr:
            oldToCopy[curr].random = oldToCopy[curr.random]
            curr = curr.next

        return dummy.next