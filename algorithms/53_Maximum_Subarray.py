#---------Tags---------
#DynamicProgramming
#Greedy
#----------------------

#---------Notes---------
# just traverse and find subarray sum
# note the biggest
# 
#-----------------------

# dp solution
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        cont_dp = []
        dp = []
        dp.append(nums[0])
        cont_dp.append(dp[0])

        for idx in range(length):
            if idx == 0:
                continue
            cont_dp.append(max(cont_dp[idx-1] + nums[idx], nums[idx]))
            dp.append(max(dp[idx-1], cont_dp[idx]))
        
        return dp[length-1]

# good enough solution
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        best_sum = nums[0]
        sum = 0

        for value in nums:
            sum += value
            if value > sum:
                sum = value
            if sum > best_sum:
                best_sum = sum
            