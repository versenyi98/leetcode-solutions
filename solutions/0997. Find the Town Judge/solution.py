from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(int)
        trusted = defaultdict(int)

        for x, y in trust:
            trusts[x] += 1
            trusted[y] += 1

        candidates = [x for x in range(1, n + 1) if trusts[x] == 0 and trusted[x] == n - 1]

        if len(candidates) == 1:
            return candidates[0]
        return -1