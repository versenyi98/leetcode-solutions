class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for letters in zip(*strs):
            if len(set(letters)) != 1:
                break
            result += letters[0]
        return result