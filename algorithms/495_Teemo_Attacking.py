#---------Tags---------
#Math
#----------------------

#---------Notes---------
# write by inspect
#-----------------------

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        length = len(timeSeries)
        if length == 0:
            return 0
        if length == 1:
            return duration

        total_duration = 0

        for idx,i in enumerate(timeSeries):
            if idx == length -1:
                total_duration += duration
            else:
                if timeSeries[idx] + duration < timeSeries[idx+1]:
                    total_duration += duration
                else:
                    total_duration += timeSeries[idx+1] - timeSeries[idx]
        
        
        return total_duration

# Good enough solution
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """

        if not timeSeries or duration == 0:
            return 0

        totalTime = 0
        start = timeSeries[0]
        end = timeSeries[0] + duration

        for i in timeSeries:
            if i > end:
                totalTime += end - start
                start = i
            end = i + duration
        # add last
        totalTime += end - start

        return totalTime        