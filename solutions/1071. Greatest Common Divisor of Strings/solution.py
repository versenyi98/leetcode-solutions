class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        so_far = ""

        for ch1, ch2 in zip(list(str1), list(str2)):
            if ch1 != ch2:
                return result
            so_far += ch1

            c1 = len(str1) % len(so_far) == 0
            c2 = len(str1) % len(so_far) == 0
            if c1 and c2:
                c3 = so_far * (len(str1) // len(so_far)) == str1
                c4 = so_far * (len(str2) // len(so_far)) == str2
                if c3 and c4:
                    result = so_far
        return result