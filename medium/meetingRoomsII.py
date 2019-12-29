import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        heap = []
        heapq.heapify(heap)
        for interval in intervals:
            if len(heap) == 0:
                heapq.heappush(heap, interval[1])
            else:
                lowEndTime = heap[0]
                if lowEndTime <= interval[0]:
                    heapq.heappop(heap)
                heapq.heappush(heap, interval[1])
        return len(heap)
