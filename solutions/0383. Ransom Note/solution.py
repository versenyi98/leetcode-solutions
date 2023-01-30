class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_arr = [0] * 26
        magazine_arr = [0] * 26

        for r in ransomNote:
            ransom_arr[ord('a') - ord(r)] += 1
        for m in magazine:
            magazine_arr[ord('a') - ord(m)] += 1

        return all(r <= m for r, m in zip(ransom_arr, magazine_arr))