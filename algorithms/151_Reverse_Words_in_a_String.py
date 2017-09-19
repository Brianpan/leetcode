#---------Tags---------
#ReverseWord
#----------------------

#---------Notes---------
# call python built in function
# 
# 
#-----------------------

# My baseline solution 
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp_s = ""
        stack = []
        for c in s:
            if c == " ":
                if tmp_s != "":
                    stack.append(tmp_s)
                    tmp_s = ""
                continue
            tmp_s += c
        
        if tmp_s != "":
            stack.append(tmp_s)
        
        return " ".join(stack[::-1])

# Good enough solution
class Solution(object):
    def revseseWords(self, s):
        return " ".join(s.split(" ")[::-1])