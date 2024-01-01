class Solution:
    def solve(self, s, i):
        if i in self.cache:
            return self.cache[i]
        if i > len(s):
            return 0
        if i == len(s):
            return 1

        val = ord(s[i]) - ord('0')
        if val == 0:
            return 0

        if val > 2:
            self.cache[i] = self.solve(s, i + 1)
            return self.cache[i]
        if val == 2 and i + 1 < len(s) and ord(s[i + 1]) - ord('0') < 7:
            self.cache[i] =  self.solve(s, i + 1) + self.solve(s, i + 2)
            return self.cache[i]
        if val == 1:
            self.cache[i] =  self.solve(s, i + 1) + self.solve(s, i + 2)
            return self.cache[i]
        self.cache[i] =  self.solve(s, i + 1)
        return self.cache[i]

    def numDecodings(self, s):
        self.cache = {}
        return self.solve(s, 0)