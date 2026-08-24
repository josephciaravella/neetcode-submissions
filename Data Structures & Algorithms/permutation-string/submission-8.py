from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)
        correct = 0

        # prep dicts
        for i in range(len(s1)):
            s1_freq[s1[i]] += 1
            s2_freq[s2[i]] += 1

        # init all chars across both dicts
        for char in ALPHABET:
            s1_freq[char] += 0
            s2_freq[char] += 0
        
        # prep exit condition
        for char in ALPHABET:
            if s1_freq[char] == s2_freq[char]:
                correct += 1

        if correct == 26:
            return True

        l,r = 0, len(s1)
        # do the work
        while r<len(s2):
            # remove freq
            s2_freq[s2[l]] -= 1
            if s2_freq[s2[l]]+1 == s1_freq[s2[l]]:
                correct -= 1
            elif s2_freq[s2[l]] == s1_freq[s2[l]]:
                correct += 1

            # add freq
            s2_freq[s2[r]] += 1
            if s2_freq[s2[r]] == s1_freq[s2[r]]:
                correct += 1
            elif s2_freq[s2[r]] == s1_freq[s2[r]]+1:
                correct -= 1

            if correct == 26:
                return True
            
            l += 1
            r += 1
        
        return False