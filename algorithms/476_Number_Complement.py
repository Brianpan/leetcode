#---------Tags---------
#BitOperator
#----------------------

#---------Notes---------
# 用adder , re 來做紀錄
# adder是要加的位元位置
# https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python
#-----------------------

# My Solution
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = num
        bit_arr = []
        while n is not 0:
            r =  0 if n % 2 == 1 else 1
            bit_arr.append(r)
            n = n >> 1
        
        return sum([i*2**idx for idx, i in enumerate(bit_arr)])

# Best Solution

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        re = 0
        # revserse used 
        adder = 1
        while(num):
            # last digit is not 1
            #
            if(not (num & 1)):
                re |= adder
            
            adder <<= 1
            num >>= 1

        return re