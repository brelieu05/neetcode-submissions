class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowMin, rowMax = 0, len(matrix) - 1

        def binarySearch(arr):
            l, r = 0, len(arr) - 1

            while l <= r:
                mid = (l + r) // 2
                print(arr[l], arr[mid])
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        while rowMin <= rowMax:
            mid = (rowMin + rowMax) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                res = binarySearch(matrix[mid])
                if res != -1:
                    return True
                else:
                    return False
            elif matrix[mid][-1] < target:
                rowMin = mid + 1
            elif matrix[mid][0] > target:
                rowMax = mid - 1
        return False