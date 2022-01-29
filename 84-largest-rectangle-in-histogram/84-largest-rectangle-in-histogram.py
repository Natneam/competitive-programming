class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                poped = stack.pop()
                max_area = max(max_area, poped[1] * (i - poped[0]))
                start = poped[0]
            stack.append((start, h))
        
        for element in stack:
            max_area = max(max_area, element[1] * (len(heights) - element[0]))
        
        return max_area
                