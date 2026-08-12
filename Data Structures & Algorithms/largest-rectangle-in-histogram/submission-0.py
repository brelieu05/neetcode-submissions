class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = [] # (height, index)

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                popped_height, popped_index = stack.pop()
                largest = max(largest, popped_height * (i - popped_index))
                start = popped_index
            stack.append((height, start))
        
        for h, i in stack:
            largest = max(largest, h * (len(heights) - i))

        return largest