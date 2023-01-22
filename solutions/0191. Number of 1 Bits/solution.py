class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([1 for power in range(32) if pow(2, power) & n])