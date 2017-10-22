#---------Company------
#Amazon
#----------------------
#---------Tags---------
#Array
#
#----------------------

#---------Notes---------
# clockwise : vertical reverse & swap
# anti-clockwise : horizontal reverse  swap
#-----------------------

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        ## clockwise
        # vertical reverse & swap
        matrix.reverse()
        for i in range(len(matrix)):
            j = i+1
            while(j < len(matrix)):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
                j += 1

        ## anti-clockwise
        # horizonal reverse & swap
        n = len(matrix)
        for i in range(len(matrix)):
            matrix[i].reverse()

        for i in range(len(matrix)):
            j = i+1
            while(j < len(matrix)):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
                j += 1