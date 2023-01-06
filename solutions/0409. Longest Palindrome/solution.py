from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        for v in counter.values():
            if ans % 2 == 0:
                ans += v
            else:
                ans += v // 2 * 2
        return ans

