#---------Tags---------
# Reduce
#----------------------

#---------Notes---------
# Use reduce to write pretty code
#-----------------------

class Solution:
    def lcp(self, str1, str2):
        i = 0
        while(i<len(str1) and i<len(str2)):
            if str1[i] == str2[i]:
                i+=1
            else:
                break

        return str1[:i]
    
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        
        if len(strs) == 1:
            return strs[0]

        return reduce(self.lcp, strs)

# My solution
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        l = len(strs) - 1
        s0 = strs[l]
        l -= 1
        while l >=0:
            tmp_s = ""
            if strs[l] == "":
                return ""
            min_len = min(len(strs[l]), len(s0))
            
            for i,c in enumerate(s0):
                # prevent IndexError
                if i >= min_len:
                    break

                if c == strs[l][i]:
                    tmp_s += c
                else:
                    break
                
            s0 = tmp_s
            
            if s0 == "":
                break
            l -= 1

        return s0