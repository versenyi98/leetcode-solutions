class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        res = 0
        for letters in zip(*strs):
            col = list(letters)
            if sorted(col) != col:
                res += 1
        return res