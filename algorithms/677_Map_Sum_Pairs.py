#---------Tags---------
#HashMap
#----------------------

#---------Notes---------
# two implement and consider what condition should use which
# 
# 
#-----------------------

# insert slow implement
# find quick
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map_dict = {}        
        self.keymap = []
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        minus = 0
        if key in self.keymap:
            minus = self.map_dict[key]
        else:
            self.keymap.append(key)

        s = ""        
        for idx in range(len(key)):
            s += key[idx]
            try:
                self.map_dict[s] +=  val - minus
            except KeyError:
                self.map_dict[s] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        try:
            return self.map_dict[prefix]
        except KeyError:
            return 0

# Insert quick
# sum slow
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map_dict = {}        
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.map_dict[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        total = 0
        prefix_len = len(prefix)
        for key in self.map_dict.keys():
            if prefix == key[:prefix_len]:
                total += self.map_dict[key]
        
        return total
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)