class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        solutions = []
        queue = [[0]]

        while queue:
            head = queue.pop(0)
            if head[-1] == len(graph) - 1:
                solutions.append(head)
                continue
            
            for edge in graph[head[-1]]:
                if edge not in head:
                    queue.append(head + [edge])

        return solutions