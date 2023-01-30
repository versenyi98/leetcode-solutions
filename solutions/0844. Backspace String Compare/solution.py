class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.perform_deletion(s) == self.perform_deletion(t)

    def perform_deletion(self, s):
        stack = []
        for char in s:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return stack