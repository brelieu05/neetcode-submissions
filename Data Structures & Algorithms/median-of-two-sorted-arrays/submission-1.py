class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1)

        median = 0
        while l <= r:
            i = (l + r) // 2
            j = half - i

            leftpartition1 = nums1[i - 1] if i > 0 else float("-inf")
            rightpartition1 = nums1[i] if i < len(nums1) else float("inf")

            leftpartition2 = nums2[j - 1] if j > 0 else float("-inf")
            rightpartition2 = nums2[j] if j < len(nums2) else float("inf")
            if leftpartition1 <= rightpartition2 and leftpartition2 <= rightpartition1:
                if total % 2:
                    return min(rightpartition1, rightpartition2)
                return ((max(leftpartition1, leftpartition2) + min(rightpartition1, rightpartition2))/ 2)
            elif leftpartition1 > rightpartition2:
                r = i - 1
            else:
                l = i + 1
                


        


        