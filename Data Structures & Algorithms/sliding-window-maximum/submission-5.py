from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        r = 0
        stack = deque()
        res = []

        # prep first window
        while r < k-1:
            while stack and nums[r] > nums[stack[-1]]:
                stack.pop()
            stack.append(r)
            r += 1

        # main loop
        for r in range(k-1, len(nums)):
            if stack and stack[0] == r-k:
                stack.popleft()
            while stack and nums[r] >= nums[stack[-1]]:
                stack.pop()
            stack.append(r)

            # add window max to res
            res.append(nums[stack[0]])

        return res