# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        self.minimum_bad = n
        self.binary_search(1, n)
        return self.minimum_bad

    def binary_search(self, lower, upper):
        if lower > upper:
            return

        center = (lower + upper) // 2

        if isBadVersion(center):
            self.minimum_bad = min(self.minimum_bad, center)
            self.binary_search(lower, center - 1)
        else:
            self.binary_search(center + 1, upper)