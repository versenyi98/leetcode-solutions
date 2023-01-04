from collections import Counter

class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        counter = Counter(tasks)
        result = 0

        for count in counter.values():
            while count % 3 != 0 and count >= 2:
                count -= 2
                result += 1
            if count % 3 != 0:
                return -1
            result += count // 3

        return result