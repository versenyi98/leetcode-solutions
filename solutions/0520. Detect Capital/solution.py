class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return all(ch.islower() for ch in word[1:]) or all(ch.isupper() for ch in word)