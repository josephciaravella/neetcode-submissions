class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        max_a = heights[0]
        
        # early exit to avoid out of bounds
        if len(heights) == 1:
            return max_a
        
        # iterate and track areas
        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                # calculate area
                if not stack:
                    max_a = max(max_a, heights[idx]*(i))
                    continue
                max_a = max(max_a, heights[idx]*((i-stack[-1])-1))
            stack.append(i)

        # empty stack
        r = len(heights)
        while stack:
            idx = stack.pop()
            
            if not stack:
                max_a = max(max_a, heights[idx]*(r))
                break
            
            max_a = max(max_a, heights[idx]*((r-stack[-1])-1))
            
        return max_a