#---------Tags---------
# DP
#----------------------

#---------Notes---------
# DP to find pattern
#-----------------------
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = []
        dp.append(0)
        dp.append(1)
        
        if num == 0:
            return [0]
        if num == 1:
            return dp
    
        pivot = 2
        offset = 1
        while(pivot <= num):
            if (2*offset) == pivot:
                offset *= 2
            
            dp.append(dp[pivot -offset]+1)
            pivot += 1    
        return dp