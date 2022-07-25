class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = list(map(lambda x: x * -1, stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            heaviest = heapq.heappop(stones) * -1
            second_heaviest = heapq.heappop(stones) * -1
            res = heaviest - second_heaviest
            if res > 0:
                heapq.heappush(stones, res * -1)
        
        if len(stones) > 0:
            return stones[0] * -1
        return 0