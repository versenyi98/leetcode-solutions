import math


class Solution:
    def dfs_from_source(self, length, source, edges):
        visited = [False] * len(edges)
        distances = [math.inf] * length

        node = source
        visited[node] = True

        distance = 0

        while True:
            distances[node] = distance
            if (node := edges[node]) == -1 or visited[node]:
                break
            visited[node] = True
            distance += 1
        return distances

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        from_node1 = self.dfs_from_source(len(edges), node1, edges)
        from_node2 = self.dfs_from_source(len(edges), node2, edges)

        best_index = -1
        best_distance = 10 * len(edges)

        for index, (dist1, dist2) in enumerate(zip(from_node1, from_node2)):
            if best_distance > max(dist1, dist2):
                best_distance = max(dist1, dist2)
                best_index = index

        return best_index
