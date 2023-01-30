class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        letters = set(list(pattern))
        mapping = {letter: set() for letter in letters}
        rev_mapping = {word: set() for word in words}

        for letter, word in zip(pattern, words):
            mapping[letter].add(word)
            rev_mapping[word].add(letter)
        return all(len(words) == 1 for words in mapping.values()) and \
               all(len(letters) == 1 for letters in rev_mapping.values())