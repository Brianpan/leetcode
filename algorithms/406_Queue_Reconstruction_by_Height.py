#---------Tags---------
#Greedy
#----------------------

#---------Notes---------
# from greatest to smallest to build the ans
#-----------------------

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        height_dict, height = {}, []
        ans = []
        for idx in range(len(people) ):
            p = people[idx]

            if p[0] not in height:
                height.append(p[0])
                height_dict[p[0]] = [(p[1], idx)]
            else:
                height_dict[p[0]].append((p[1], idx))
        
        sorted_height = sorted(height, reverse=True)
        for h in sorted_height:
            # from smallest to insert
            height_dict[h].sort()
            for item in height_dict[h]:
                ans.insert(item[0], people[item[1]])
        
        return ans