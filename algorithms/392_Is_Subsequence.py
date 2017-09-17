#---------Tags---------
#BinarySearch
#Greedy
#----------------------

#---------Notes---------
# use Python find to implement binary search
# 
# 
#-----------------------

# Greedy
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        s_list = list(s)
        isSub = False
        for t_char in t:
            if t_char == s_list[0]:
                s_list.pop(0)
                if len(s_list) == 0:
                    isSub = True
                    break
        
        return isSub

# Binary Search
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False

        s_idx = 0
        isSub = True
        for s_char in s:
            if s_idx != 0:
                s_idx = t.find(s_char, s_idx+1)
            else:
                s_idx = t.find(s_char, s_idx)
            
            if s_idx == -1:
                isSub = False
                break

        return isSub