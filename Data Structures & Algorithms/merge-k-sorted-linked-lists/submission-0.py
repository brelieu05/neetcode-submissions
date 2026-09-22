# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heap.append((node.val, i, node))

        heapq.heapify(heap)   

        dummy = curr = ListNode()

        while heap:
            
            val, i, node = heapq.heappop(heap)

            nextNode = node.next

            if nextNode:
                heapq.heappush(heap, (nextNode.val, i, nextNode))
            
            curr.next = ListNode(val)
            curr = curr.next


        return dummy.next