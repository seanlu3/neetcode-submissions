class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            hmap = {}
            for num in nums:
                hmap[num] = 1 + hmap.get(num, 0)

            minHeap = []
            for num in hmap.keys():
                heapq.heappush(minHeap, (hmap[num], num))

                if len(minHeap) > k:
                    heapq.heappop(minHeap)
            
            result = []
            for i in range(k):
                result.append(heapq.heappop(minHeap)[1])
            
            return result