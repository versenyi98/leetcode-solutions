class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letter_idxs = [idx for idx, char in enumerate(s) if char.isalpha()]
        letter_count = len(letter_idxs)

        results = []

        lower = s.lower()

        for transformation_id in range(pow(2, letter_count)):
            results.append(lower)
            for i, letter_idx in enumerate(letter_idxs):
                if pow(2, i) & transformation_id:
                    prefix = results[-1][:letter_idx]
                    letter = results[-1][letter_idx].upper()
                    suffix = results[-1][letter_idx + 1:]

                    results[-1] = prefix + letter + suffix
        return results