class Solution:
    def dp(self, i, k):
        if k == 0:
            return 0

        if i == len(self.s):
            return 0

        if self.cache[k][i] != -1:
            return self.cache[k][i]

        ni = bisect_right(self.s, self.e[i])
        self.cache[k][i] = max(self.dp(ni, k - 1) + self.p[i], self.dp(i + 1, k))
        return self.cache[k][i]

    def maxValue(self, events: List[List[int]], k: int) -> int:
        self.s = []
        self.e = []
        self.p = []

        self.cache = []
        for i in range(k + 1):
            self.cache.append([-1] * len(events))

        for s, e, p in sorted(events):
            self.s.append(s)
            self.e.append(e)
            self.p.append(p)

        return self.dp(0, k)