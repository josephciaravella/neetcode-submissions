from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_f = defaultdict(int)
        t_f = defaultdict(int)

        for i in range(len(s)):
            s_f[s[i]] += 1
            t_f[t[i]] += 1

        return s_f == t_f