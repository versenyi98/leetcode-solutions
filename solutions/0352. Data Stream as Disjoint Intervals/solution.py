import bisect


class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        new_interval = [value, value]
        pos = bisect.bisect_right(self.intervals, new_interval)

        if len(self.intervals) == 0:
            self.intervals.append(new_interval)
            return None

        if pos == len(self.intervals):
            begin, end = self.intervals[-1]
            if begin <= value <= end:
                return None
            if value == end + 1:
                self.intervals[-1][1] = value
            else:
                self.intervals += [new_interval]
            return None
        if pos == 0:
            begin, end = self.intervals[0]
            if begin <= value <= end:
                return None
            if value == begin - 1:
                self.intervals[0][0] = value
            else:
                self.intervals = [new_interval] + self.intervals
            return None

        dbegin, dend = self.intervals[pos - 1]
        if dbegin <= value <= dend:
            return None

        ubegin, uend = self.intervals[pos]

        if dend == value or ubegin == value:
            return None
        if dend + 1 == value == ubegin - 1:
            self.intervals[pos - 1: pos + 1] = [[dbegin, uend]]
        elif dend + 1 == value:
            self.intervals[pos - 1] = [dbegin, value]
        elif ubegin - 1 == value:
            self.intervals[pos] = [value, uend]
        else:
            self.intervals = self.intervals[:pos] + [new_interval] + self.intervals[pos:]

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()