#---------Tags---------
#BinarySearch
#----------------------

#---------Notes---------
# notice the boundary
# 
#-----------------------

class Solution(object):
    def binarySearch(self, nums, left, right):
        if left == right -1:
            return nums[left]
                
        mid = (left+right)/2
        # position odd
        # if is normal it would be different from the previous node
        if mid %2 == 0:
            if nums[mid] != nums[mid-1]:
                return self.binarySearch(nums, mid, right)
            else:
                return self.binarySearch(nums, left, mid)
    
        # position even
        # if is normal it would be the same as the previous node
        else:
            if nums[mid] != nums[mid-1]:
                return self.binarySearch(nums, left, mid)
            else:
                return self.binarySearch(nums, mid, right)
            
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[1]
        
        return self.binarySearch(nums, 0, len(nums))