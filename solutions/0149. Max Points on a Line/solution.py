import math


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maximum = 0
        for [px, py] in points:
            slopes = {}
            for [ox, oy] in points:
                if ox == px and oy == py:
                    continue
                first, second = sorted([(px, py), (ox, oy)])
                x_diff = first[0] - second[0]
                y_diff = first[1] - second[1]

                if x_diff == 0:
                    slope = 0
                elif y_diff == 0:
                    slope = math.inf
                else:
                    slope = y_diff / x_diff
                if slope not in slopes:
                    slopes[slope] = 1
                else:
                    slopes[slope] += 1
                maximum = max(max(slopes.values()), maximum)
        return maximum + 1