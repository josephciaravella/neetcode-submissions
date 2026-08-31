from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char)-ord('a')] += 1
            
            d1[tuple(count)].append(word)


        return list(d1.values())