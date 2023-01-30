class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_arr = [0] * 26
        s2_arr = [0] * 26

        for s in s1:
            s1_arr[ord('a') - ord(s)] += 1

        for s in s2[:len(s1)]:
            s2_arr[ord('a') - ord(s)] += 1

        for idx in range(len(s2) - len(s1)):
            if s1_arr == s2_arr:
                return True

            s2_arr[ord('a') - ord(s2[idx])] -= 1
            s2_arr[ord('a') - ord(s2[idx + len(s1)])] += 1
        else:
            if s1_arr == s2_arr:
                return True
        return False
