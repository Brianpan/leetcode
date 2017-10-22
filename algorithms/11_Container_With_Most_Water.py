#---------Tags---------
#TwoPointer
#----------------------

#---------Notes---------
# should know what the problem said
#-----------------------

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 1:
            return 0
        first = True
        maxContainer = 0
        l = 0
        r = len(height) - 1
        while l < r:
            hl = height[l]
            hr = height[r]
            container = (r-l)*min(hl, hr)
            maxContainer = container if container > maxContainer else maxContainer
            if height[l] >= height[r]:
                prev = height[r]
                while r > l and prev >= height[r]:
                    r -= 1
            elif height[r] > height[l]:
                prev = height[l]
                while r > l and prev >= height[l]:
                    l += 1
            
        
        
        return maxContainer