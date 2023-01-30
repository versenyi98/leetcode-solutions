class Solution:
    def reverseBits(self, n: int) -> int:
        return sum([pow(2, 31 - i) for i in range(32) if pow(2, i) & n])