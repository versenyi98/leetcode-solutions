class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True

        mapping = {ch: i for i, ch in enumerate(order)}

        for i, word in enumerate(words[:-1]):
            next_word = words[i + 1]
            indexes = [mapping[ch] for ch in word]
            next_indexes = [mapping[ch] for ch in next_word]
            if next_indexes < indexes:
                return False

        return True