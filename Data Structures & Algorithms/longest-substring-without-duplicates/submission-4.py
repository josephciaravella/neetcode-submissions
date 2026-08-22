class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        l,r = 0,0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            
            max_len = max(max_len, len(seen))
            r += 1
        
        return max_len