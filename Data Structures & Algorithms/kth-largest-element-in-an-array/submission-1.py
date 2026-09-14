class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify_max(nums)
        
        return heapq.nlargest(k, heap)[-1]