from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        mfc = s[0]
        l,r = 0,0
        max_len = 0

        while r < len(s):
            # add char to freq
            freq[s[r]] += 1
            # evaluate mfc
            mfc = max(freq, key=freq.get)
            # >k swaps needed?
            while r+1-l > freq[mfc]+k:
                freq[s[l]] -= 1
                # evaluate mfc
                mfc = max(freq, key=freq.get)
                l+=1
            # calculate max_len
            max_len = max(max_len, r+1-l)
            # move r
            r+=1

        return max_len