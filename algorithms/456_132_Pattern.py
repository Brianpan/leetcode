#---------Tags---------
#Stack
#----------------------

#---------Notes---------
# Use stack to trace
#-----------------------

class Solution(object):

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s3 = -999999999
        stack = []
        
        for i in nums[::-1]:
            if i < s3:
                return True
            # track which is smaller than current pos
            # stack put all larger than current position
            while(len(stack) > 0 and i > stack[-1]):
                if s3 < stack[-1]:
                    s3 = stack[-1]
                stack.pop()
            
            stack.append(i)
        
        return False