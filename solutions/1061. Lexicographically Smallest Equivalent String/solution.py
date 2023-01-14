class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        groups = [[chr(ord('a') + idx)] for idx in range(26)]
        mapping = {chr(ord('a') + idx): idx for idx in range(26)}

        for ch1, ch2 in zip(s1, s2):
            group_idx1 = mapping[ch1]
            group_idx2 = mapping[ch2]

            if group_idx1 == group_idx2:
                continue

            group2 = groups[group_idx2]

            for ch in group2:
                mapping[ch] = group_idx1

            groups[group_idx1].extend(group2)
            groups[group_idx2] = []
        groups = [sorted(group) for group in groups]

        return "".join([groups[mapping[ch]][0] for ch in baseStr])
