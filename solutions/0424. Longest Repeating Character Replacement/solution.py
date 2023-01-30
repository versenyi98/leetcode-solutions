def ctoi(char):
    return ord(char) - ord('A')


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        values = [0] * 26

        start = 0
        end = 0
        result = 0

        while end != len(s):
            values[ctoi(s[end])] += 1
            if max(values) + k < end - start + 1:
                values[ctoi(s[start])] -= 1
                start += 1
            else:
                result = max(result, end - start + 1)
            end += 1

        return result
