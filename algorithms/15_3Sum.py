#---------Company------
#Amazon
#----------------------
#---------Tags---------
#2 Pointer
#----------------------

#---------Notes---------
# Carefully use 2 pointer to point left and right
#-----------------------

# Normal Solution using 2 pointers
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range( len(nums) - 2 ):
            if i > 0:
                if nums[i-1] == nums[i]:
                    continue
            l,r = i+1, len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l+1 < len(nums) and nums[l] == nums[l+1]:
                        l += 1
                    while r-1 > 0 and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans