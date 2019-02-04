"""
22. Given a mxn matrix, if an element is 0, set its entire row and col to 0.(Do it inplace)
"""

def zeroing_rows_and_cols(matrix):
    rows = []
    cols = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)
    for r in rows:
        for c in range(len(matrix[0])):
            matrix[r][c] = 0
    for c in cols:
        for r in range(len(matrix)):
            matrix[r][c] = 0



