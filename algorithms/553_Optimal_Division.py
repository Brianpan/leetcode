#---------Tags---------
#Math
#----------------------

#---------Notes---------
# investigate the patterns
# 
# 
#-----------------------

# My Solution
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])

        init_v = nums.pop(0)
        s_list = map(lambda x: str(x), nums)
        if len(nums) == 1:
            return str(init_v) + "/" + s_list[0]
        else:
            return str(init_v) + "/" + "("+ "/".join(s_list) + ")"

# Good Enough solution
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        str_s = map(str, nums)
        if len(nums) <= 2:
            return "/".join(str_s)

        return "{}/({})".format( str_s[0], "/".join(str_s[1:]) )