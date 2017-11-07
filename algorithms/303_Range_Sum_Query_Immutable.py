#---------Tags---------
# DP
#----------------------

#---------Notes---------
# DP trick : dp is the sum of the node before indexess
#-----------------------

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = nums
        i = 1
        n = len(nums)
        while i < n:
            self.dp[i] += nums[i-1]
            i += 1
                    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.dp[j]
        return self.dp[j] - self.dp[i-1]
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)