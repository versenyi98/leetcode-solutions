import bisect
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        lis = []

        for element in s:
            idx = bisect.bisect_right(lis, element)
            if idx == len(lis):
                lis.append(element)
            else:
                lis[idx] = element

        return len(s) - len(lis)