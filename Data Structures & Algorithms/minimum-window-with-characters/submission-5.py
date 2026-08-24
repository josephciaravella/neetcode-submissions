class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_f, t_f = {}, {}
        correct = 0
        shortest = ""
        l, r = 0, 0

        # build t freq dict
        for char in t:
            t_f[char] = t_f.get(char, 0) + 1

        while r<len(s):
            # add char to freq list
            s_f[s[r]] = s_f.get(s[r], 0) + 1
            if s[r] in t_f and s_f[s[r]] == t_f[s[r]]:
                correct += 1

            while correct == len(t_f):
                # 1. Update shortest string if current window is smaller
                if not shortest or (r - l + 1) < len(shortest):
                    shortest = s[l:r+1]
                
                # 2. Remove left character from window
                s_f[s[l]] -= 1
                
                # 3. Check if removing it broke a required match
                if s[l] in t_f and s_f[s[l]] < t_f[s[l]]:
                    correct -= 1
                    
                # 4. Slide left pointer forward
                l += 1
            r += 1

        return shortest