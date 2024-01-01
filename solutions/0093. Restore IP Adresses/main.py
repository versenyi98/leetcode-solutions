class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        n = len(s)

        for i in range(1, n):
            segment1 = s[:i]
            for j in range(i + 1, n):
                segment2 = s[i:j]
                for k in range(j + 1, n):
                    segment3 = s[j:k]
                    segment4 = s[k:]

                    segments = [segment1, segment2, segment3, segment4]

                    if all((segment[0] != '0' or len(segment) == 1) and 0 <= int(segment) <= 255 for segment in segments):
                        results.append(segment1 + '.' + segment2 + '.' + segment3 + '.' + segment4)
        return results