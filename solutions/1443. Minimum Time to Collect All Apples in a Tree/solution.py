class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.result = 0
        self.edges = edges
        self.connections = {i: [] for i in range(n)}
        self.has_apple = hasApple
        self.visited = set()
        for f, t in edges:
            self.connections[f].append(t)
            self.connections[t].append(f)
        self.subtree_has_apple(0)

        return self.result

    def subtree_has_apple(self, root):
        self.visited.add(root)
        result = self.has_apple[root]
        for other in self.connections[root]:
            if other not in self.visited:
                result = self.subtree_has_apple(other) or result
        if result and root:
            self.result += 2
        return result