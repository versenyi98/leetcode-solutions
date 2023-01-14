class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.connections = {i: [] for i in range(len(parent))}
        self.s = s
        self.visited = set()
        self.result = 0

        for i, p in enumerate(parent):
            if p == -1:
                root = i
            else:
                self.connections[p].append(i)

        self.traverse(root, '')
        return self.result

    def traverse(self, root, parent_label):
        label = self.s[root]

        best = 0
        second_best = 0

        for other in self.connections[root]:
            other_res = self.traverse(other, label)
            if other_res >= best:
                second_best = best
                best = other_res
            elif other_res > second_best:
                second_best = other_res

        self.result = max(self.result, 1 + best + second_best)

        if parent_label == label:
            return 0
        else:
            return best + 1