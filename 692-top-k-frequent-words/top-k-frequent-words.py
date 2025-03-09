class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for key, freq in count.items():
            heapq.heappush(heap, [-freq, key])

        return [heappop(heap)[1] for _ in range(k)]