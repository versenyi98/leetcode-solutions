class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        positions = defaultdict(list)

        for i, ch in enumerate(s):
            positions[ch].append(i)

        maximum = -1
        for values in positions.values():
            if len(values) > 0:
                maximum = max(maximum, values[-1] - values[0] - 1)
        return maximum