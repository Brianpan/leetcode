#---------Tags---------
#DFS
#----------------------

#---------Notes---------
# do not consider bad case
#-----------------------

# Basic DFS
class Solution(object):
    def traverseBattle(self, board, i, j, m, n):
        if board[j][i] == "X":
            board[j][i] = "."
            for p in [(0,1),(1,0),(-1,0),(0,-1)]:
                next_i = i + p[0]
                next_j = j + p[1]
                if next_i < n and next_j < m and next_i >= 0 and next_j >= 0:
                    self.traverseBattle(board,next_i, next_j, m, n)
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        battle_num = 0
        m = len(board)
        n = len(board[0])
        for j in range(m):
            for i in range(n):
                if board[j][i] == "X":
                    self.traverseBattle(board, i, j, m, n)
                    battle_num += 1
        
        return battle_num

# Clean solution
class Solution(object):
    
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        battle_num = 0
        m = len(board)
        n = len(board[0])
        for j in range(m):
            for i in range(n):
                if board[j][i] == "X":
                    if ( i == 0 or board[j][i-1] == ".") and ( j == 0 or board[j-1][i] == "."):
                        battle_num += 1
        
        return battle_num