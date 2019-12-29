class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if len(intervals) == 0 or len(intervals) == 1:
            return True
        intervals.sort()
        endTime = intervals[0][1]
        for i in range(1, len(intervals)):
            if endTime > intervals[i][0]:
                return False
            else:
                endTime = intervals[i][1]
        return True
