class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        times = set()
        for item in intervals:
            for i in range(item[0], item[1]):
                if i in times:
                    return False
                times.add(i)
        return True