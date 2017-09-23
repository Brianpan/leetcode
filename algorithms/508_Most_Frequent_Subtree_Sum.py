#---------Tags---------
#TreeTreverse
#UseParams
#----------------------

#---------Notes---------
# When using dict key existing or not, please use get to check it
#-----------------------

# My Solution beats 80%
class Solution(object):
    def buildRangeSum(self, node, ans_dict):
        tmp = 0
        if not node:
            return
        
        if node.left is not None: 
            self.buildRangeSum(node.left, ans_dict)
            tmp += node.left.val
        if node.right is not None:
            self.buildRangeSum(node.right, ans_dict)
            tmp += node.right.val
        
        node.val += tmp
        # use get to increase efficiency
        ans_dict[node.val] = ans_dict.get(node.val, 0) + 1
        
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans_dict = {}
        self.buildRangeSum(root, ans_dict)
        
        # treverse dict
        ans_list = []
        freq = ans_dict.values()
        if len(freq) == 0:
            return ans_list

        max_freq = max(freq)
        for k,v in ans_dict.items():
            if v == max_freq:
                ans_list.append(k)
        return ans_list