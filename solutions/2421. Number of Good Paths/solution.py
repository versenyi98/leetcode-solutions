class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        result = len(vals)
        parent = list(range(len(vals)))
        count = [{vals[i]: 1} for i in range(len(vals))]
        edges = sorted([max(vals[i], vals[j]), i, j] for i,j in edges)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for v, i, j in edges:
            parent_i, parent_j = find(i), find(j)
            count_i, count_j = count[parent_i].get(v, 0), count[parent_j].get(v, 0)
            result += count_i * count_j
            parent[parent_j] = parent_i
            count[parent_i][v] = count_i + count_j
        return result