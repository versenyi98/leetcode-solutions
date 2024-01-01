class Solution:
    def dp(self, current, toBeRemoved, previous, previousCount):
        if toBeRemoved < 0:
            return 1000000000
        
        if current == len(self.s):
            return 0

        key = (current, toBeRemoved, previous, previousCount)
        if key in self.cache:
            return self.cache[key]

        removed = self.dp(current + 1, toBeRemoved - 1, previous, previousCount)
        kept = 0

        if self.s[current] == previous:
            kept = self.dp(current + 1, toBeRemoved, previous, previousCount + 1)
            kept += 1 if (previousCount in [1, 9, 99]) else 0
        else:
            kept = 1 + self.dp(current + 1, toBeRemoved, self.s[current], 1)
        self.cache[key] = min(kept, removed)

        return self.cache[key]

    def getLengthOfOptimalCompression(self, s, k):
        self.s = s
        self.cache = {}

        return self.dp(0, k, None, 0)