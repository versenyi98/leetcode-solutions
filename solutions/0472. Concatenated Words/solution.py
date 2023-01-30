class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        result = set()
        vocab = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                if prefix not in vocab:
                    continue

                suffix = word[i:]
                if suffix in vocab or dfs(suffix):
                    return True
            return False

        for word in words:
            if dfs(word):
                result.add(word)
        return list(result)
