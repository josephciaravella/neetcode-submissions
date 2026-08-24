class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_f, t_f = {}, {}
        good_chars = set()
        shortest = s
        l,r = 0,0

        # build t freq dict
        for char in t:
            t_f[char] = t_f.get(char, 0) + 1

        while r<len(s):
            # add char to freq list
            s_f[s[r]] = s_f.get(s[r], 0) + 1

            # evaluate correct
            if s[r] in t_f and s_f[s[r]] == t_f[s[r]] and s[r] not in good_chars:
                good_chars.add(s[r])

            # we have more than necessary, cut 
            if s[r] in t_f and s_f[s[r]] > t_f[s[r]]:
                while s[l] not in t_f or s_f[s[l]] > t_f[s[l]]:
                    s_f[s[l]] -= 1
                    if not s_f[s[l]]:
                        del s_f[s[l]]
                    l += 1

            # all correct, move left and check for shortest string
            if len(good_chars) == len(t_f):
                while s[l] not in t_f:
                    s_f[s[l]] -= 1
                    if not s_f[s[l]]:
                        del s_f[s[l]]
                    l += 1
                if len(s[l:r+1]) < len(shortest):
                    shortest = s[l:r+1]

            r += 1
                
        if len(shortest) == len(s) and len(good_chars) != len(t_f):
            return ''

        return shortest