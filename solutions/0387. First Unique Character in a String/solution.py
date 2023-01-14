from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        unique = list(filter(lambda x: x[1] == 1, counter.items()))
        if len(unique) == 0:
            return -1
        return s.index(unique[0][0])