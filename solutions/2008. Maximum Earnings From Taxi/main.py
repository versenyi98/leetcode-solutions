class Solution:
    def dp(self, i):
        if i == len(self.s):
            return 0

        if self.cache[i] != -1:
            return self.cache[i]

        ni = bisect_left(self.s, self.e[i])
        self.cache[i] = max(self.dp(ni) + self.p[i], self.dp(i + 1))
        return self.cache[i]

    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        self.s = []
        self.e = []
        self.p = []

        self.cache = [-1] * len(rides)

        for s, e, p in sorted(rides):
            self.s.append(s)
            self.e.append(e)
            self.p.append(e - s + p)

        return self.dp(0)