class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            # stack not empty and violates the monotonic stack we want
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i-idx
            stack.append(i)
        
        return res