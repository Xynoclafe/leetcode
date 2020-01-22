import heapq
class Solution(object):
    def reorganizeString(self, S):
        heap = [(-S.count(i), i) for i in set(S)]
        heapq.heapify(heap)
        
        if any(-count > (len(S) + 1) / 2 for count, element in heap):
            return ""
        
        outList = []
        while len(heap) >= 2:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)
            if not outList or char1 != outList[-1]:
                outList.extend([char1, char2])
            else:
                outList.extend([char2, char1])
                
            if count1 + 1:
                heapq.heappush(heap, (count1 + 1, char1))
            if count2 + 1:
                heapq.heappush(heap, (count2 + 1, char2))
        
        return "".join(outList) + (heap[0][1] if heap else "")
