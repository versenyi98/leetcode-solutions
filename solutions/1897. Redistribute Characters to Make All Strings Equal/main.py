class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = {}

        for word in words:
            for ch in word:
                if ch in counts:
                    counts[ch] += 1
                else:
                    counts[ch] = 1

        return all([value % len(words) == 0 for value in counts.values()])