class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cases = pow(2, len(s) - 1)
        results = []
        for case in range(cases):
            last = 0
            segments = []
            for m in range(len(s) - 1):
                if pow(2, m) & case:
                    segments.append(s[last:m + 1])
                    last = m + 1
            segments.append(s[last:])
            if all(segment == segment[::-1] for segment in segments):
                results.append(segments)
        return results