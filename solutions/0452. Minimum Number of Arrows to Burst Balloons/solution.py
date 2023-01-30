class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points = sorted(points)
        end = points[0][1]
        start = points[0][0]
        result = 1
        for [p_start, p_end] in points[1:]:
            if start <= p_start <= end or start <= p_end <= end or (start < p_start and end > p_end):
                start = max(start, p_start)
                end = min(end, p_end)
            else:
                start = p_start
                end = p_end
                result += 1
        return result
