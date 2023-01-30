class Solution:
    def fib_rec(self, n):
        if self.memo[n] == -1:
            self.memo[n] = self.fib_rec(n - 1) + self.fib_rec(n - 2)
        return self.memo[n]

    def fib(self, n: int) -> int:
        self.memo = [-1] * (n + 2)
        self.memo[0] = 0
        self.memo[1] = 1

        return self.fib_rec(n)
