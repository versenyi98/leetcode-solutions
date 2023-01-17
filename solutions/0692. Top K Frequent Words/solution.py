from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)

        words_with_counts = ([(-count, word) for word, count in counter.items()])
        heapify(words_with_counts)

        result = []

        while k:
            k -= 1
            count, word = heappop(words_with_counts)
            result.append(word)

        return result
