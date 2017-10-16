#---------Company------
#Amazon
#----------------------
#---------Tags---------
#Set
#BFS
#----------------------

#---------Notes---------
# Use set to implement BFS
#-----------------------

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        
        neighbor_pairs = [[0,1],[1,0], [0,-1], [-1,0]]
        row = len(grid)
        stack_set = set([])
        lands = 0
        
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                pair = (i, j)
                if grid[i][j] == '0':
                    continue
                
                stack_set.add(pair)    
                lands += 1
                while( len(stack_set) > 0 ):
                    pair = stack_set.pop()
                    for p in neighbor_pairs:
                        new_i = pair[0] + p[0]
                        new_j = pair[1] + p[1]

                        if new_i < 0 or new_j < 0 or new_i >= row or new_j >= col:
                            continue
                        if grid[new_i][new_j] == '1':
                            grid[new_i][new_j] = '0'
                            stack_set.add((new_i, new_j))
                                
        return lands