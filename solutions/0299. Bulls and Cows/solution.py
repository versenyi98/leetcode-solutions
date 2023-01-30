class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        secret_numbers = Counter()
        guess_numbers = Counter()

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_numbers.update(s)
                guess_numbers.update(g)

        for g, c in guess_numbers.items():
            cows += min(c, secret_numbers.get(g, 0))

        return f"{bulls}A{cows}B"
