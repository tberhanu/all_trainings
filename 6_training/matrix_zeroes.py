""" Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
"""
def setZeroes(matrix):
    row = set()
    col = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)

    for i in row:
        for j in range(len(matrix[i])):
            matrix[i][j] = 0
    for i in col:
        for j in range(len(matrix)):
            matrix[j][i] = 0
