class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        new_begin, new_end = newInterval
        for idx, (begin, end) in enumerate(intervals):
            if end < new_begin:
                continue

            if begin > new_end:
                return intervals[:idx] + [newInterval] + intervals[idx:]

            if begin <= new_begin <= new_end <= end:
                return intervals

            if new_begin <= begin <= new_end <= end:
                return intervals[:idx] + [[new_begin, end]] + intervals[idx + 1:]

            if (begin_val := min(begin, new_begin)) <= end <= new_end:
                begin_idx = idx

                for idx, (begin, end) in enumerate(intervals[begin_idx + 1:], begin_idx + 1):
                    if begin <= new_end <= end:
                        return intervals[:begin_idx] + [[begin_val, end]] + intervals[idx + 1:]
                    if new_end < begin:
                        return intervals[:begin_idx] + [[begin_val, new_end]] + intervals[idx:]
                return intervals[:max(0, begin_idx)] + [[begin_val, new_end]]
        return intervals + [newInterval]