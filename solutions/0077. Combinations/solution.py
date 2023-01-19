class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        queue = [[i] for i in range(1, n + 2 - k)]
        result = []

        while queue:
            head = queue.pop(0)

            if len(head) == k:
                result.append(head)
                continue

            for i in range(head[-1] + 1, n + 2 - (k - len(head))):
                next_ = head + [i]
                if len(next_) == k:
                    result.append(next_)
                else:
                    queue.append(next_)
        return result
