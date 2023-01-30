class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flattened = []
        for row in mat:
            flattened.extend(row)

        if len(flattened) != r * c:
            return mat

        return [flattened[i * c:(i + 1) * c] for i in range(r)]