from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = {}
        s_dict = {}
        for idx in range(26):
            p_dict[chr(ord('a') + idx)] = 0
            s_dict[chr(ord('a') + idx)] = 0
        for key, value in dict(Counter(p)).items():
            p_dict[key] = value
        for key, value in dict(Counter(s[:len(p)])).items():
            s_dict[key] = value

        result = []

        idx = -1
        for idx in range(len(s) - len(p)):
            if s_dict == p_dict:
                result.append(idx)
            s_dict[s[idx]] -= 1
            s_dict[s[idx + len(p)]] += 1
        else:
            if s_dict == p_dict:
                result.append(idx + 1)
        return result
