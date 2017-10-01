#---------Tags---------
#DFS
#Queue
#----------------------

#---------Notes---------
#Use hashtable to note or use queue
#-----------------------
# My Solution
class Solution(object):
    def dfs(self, board, note, m, n, click):
        y = click[0]
        x = click[1]
                
        # out of the board
        if y >= m or x >= n or y < 0 or x < 0:
            return
        # check is done or not
        if note[y][x]:
            return
        note[y][x] = 1
        
        if board[y][x] == "M":
            board[y][x] = "X"
            return
        if board[y][x] == "E":
            has_mine = 0
            # with mine near case
            for y_move in [-1, 0, 1]:
                for x_move in [-1, 0, 1]:
                    if y_move == 0 and x_move == 0:
                        continue
                    if y + y_move >= m or x+x_move >= n or y + y_move < 0 or x + x_move < 0:
                        continue
                    if board[y+y_move][x+x_move] == "M":
                        has_mine += 1
            
            if has_mine > 0:
                board[y][x] = str(has_mine)
                return
            
            # no mine near case
            board[y][x] = "B"
        
            for move in [[-1,0], [1,0], [0,-1], [0,1], [1,1], [-1,-1],[1,-1],[-1,1]]:
                x_move = move[1]
                y_move = move[0]
                    
                if y + y_move >= m or x+x_move >= n or y + y_move < 0 or x + x_move < 0:
                    continue
                self.dfs(board, note, m, n, [y+y_move, x+x_move])
            
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m = len(board)
        n = len(board[0])
        note = []
        for j in range(m):
            note.append([None]*n)
        self.dfs(board, note, m, n, click)
        return board

# My Solution
class Solution(object):
    def dfs(self, board, note, m, n, click):
        y = click[0]
        x = click[1]
                
        # out of the board
        if y >= m or x >= n or y < 0 or x < 0:
            return
        
        if board[y][x] == "M":
            board[y][x] = "X"
            return
        if board[y][x] == "E":
            has_mine = 0
            # with mine near case
            for y_move in [-1, 0, 1]:
                for x_move in [-1, 0, 1]:
                    if y_move == 0 and x_move == 0:
                        continue
                    if y + y_move >= m or x+x_move >= n or y + y_move < 0 or x + x_move < 0:
                        continue
                    if board[y+y_move][x+x_move] == "M":
                        has_mine += 1
            
            if has_mine > 0:
                board[y][x] = str(has_mine)
                return
            
            # no mine near case
            board[y][x] = "B"
        
            for move in [[-1,0], [1,0], [0,-1], [0,1], [1,1], [-1,-1],[1,-1],[-1,1]]:
                x_move = move[1]
                y_move = move[0]
                    
                if y + y_move >= m or x+x_move >= n or y + y_move < 0 or x + x_move < 0:
                    continue
                self.dfs(board, m, n, [y+y_move, x+x_move])
            
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m = len(board)
        n = len(board[0])
        note = []
        for j in range(m):
            note.append([None]*n)
        self.dfs(board, note, m, n, click)
        return board

# Queue approach
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m = len(board)
        n = len(board[0])
        q = [click]
        while(len(q) > 0):
            y, x = q.pop(0)
            if board[y][x] == "M":
                board[y][x] = "X"
                continue
            if board[y][x] == "E":
                has_mine = 0
                # with mine near case
                for y_move in [-1, 0, 1]:
                    for x_move in [-1, 0, 1]:
                        if y_move == 0 and x_move == 0:
                            continue
                        if y + y_move >= m or x+x_move >= n or y + y_move < 0 or x + x_move < 0:
                            continue
                        if board[y+y_move][x+x_move] == "M":
                            has_mine += 1
            
                if has_mine > 0:
                    board[y][x] = str(has_mine)
                    continue
            
                # no mine near case
                board[y][x] = "B"

                for move in [[-1,0], [1,0], [0,-1], [0,1], [1,1], [-1,-1],[1,-1],[-1,1]]:
                    x_move = move[1]
                    y_move = move[0]

                    if y + y_move >= m or x+x_move >= n or y + y_move < 0 or x + x_move < 0:
                        continue
                    q.append([y+y_move,x+x_move])
        
        return board