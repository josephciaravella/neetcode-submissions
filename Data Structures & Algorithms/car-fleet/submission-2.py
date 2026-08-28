import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = []

        # group pairs
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        # sort pairs by distance (descending)
        pairs.sort(reverse=True)
        
        # add to stack
        for pair in pairs:
            p, v = pair
            time = (target-p)/v
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)