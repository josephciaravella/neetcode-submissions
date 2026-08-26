class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r = 0,0
        w_max = -10001
        timer = 0
        res = []

        # prep first window
        while r < k-1:
            if nums[r] >= w_max:
                w_max = nums[r]
                timer = k
            timer -= 1
            r += 1

        # main loop
        while r < len(nums):
            # new/same max found, set it and reset timer
            if nums[r] >= w_max:
                w_max = nums[r]
                timer = k
            else:
                # no time left, look for a new max in the window
                if not timer:
                    temp = l
                    w_max = nums[r]
                    timer = k
                    while temp < r:
                        if nums[temp] >= w_max:
                            w_max = nums[temp]
                            timer = k-(r-temp)
                        temp += 1
                    # have a new max now

            # timer still gt 0 -> decrease timer
            timer -= 1
            
            # shift window
            l += 1
            r += 1

            # add window max to res
            res.append(w_max)

        return res