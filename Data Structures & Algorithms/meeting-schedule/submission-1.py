
# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        interval_list = []
        sum_intervals = 0

        if not intervals:
            return True
            
        for i in intervals:
            x, y = i.start, i.end
            interval_list.append(x)
            interval_list.append(y)
            sum_intervals += (y-x)
        
        max_ = max(interval_list)
        min_ = min(interval_list)

        if (max_- min_) < sum_intervals:
            return False
        else:
            return True
            



