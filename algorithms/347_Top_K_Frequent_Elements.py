#---------Tags---------
#Hashmap
#----------------------

#---------Notes---------
# Use dict to sort and return
#-----------------------

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_dict = {}
        top_k = []
        for i in nums:
            try: 
                num_dict[i] += 1
            except KeyError:
                num_dict[i] = 1
        
        sorted_count = sorted(num_dict.items(), key=(lambda x:x[1]), reverse=True)
        
        return [p[0] for p in sorted_count[:k]]