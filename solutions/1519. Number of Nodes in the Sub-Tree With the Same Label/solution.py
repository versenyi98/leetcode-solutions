from operator import add


def ctoi(c):
    return ord(c) - ord('a')


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        result = [0] * n
        connections = {i: [] for i in range(n)}
        visited = set()
        for f, t in edges:
            connections[f].append(t)
            connections[t].append(f)

        def traverse(root):
            subtree_res = [0] * 26
            subtree_res[ctoi(labels[root])] += 1

            visited.add(root)

            for other in connections[root]:
                if other not in visited:
                    child_subtree_res = traverse(other)
                    subtree_res = list(map(add, subtree_res, child_subtree_res))
            result[root] = subtree_res[ctoi(labels[root])]
            return subtree_res

        traverse(0)
        return result


