"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal,
switching the row and column indices of the matrix.
Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""

def transpose(matrix):
    """ Runtime: 64 ms, faster than 57.33% of Python3 online submissions for Transpose Matrix.

    The following line will zip the UNPACKED matrix which will return the transposed
     matrix but with each row as a tuple rather than as a list"""
    zipped = zip(* matrix)
    """ Remember 'list' is a function, so use 'map' to change all the tuples to list"""
    zipped = list(zipped)
    zipped = map(list, zipped)
    return list(zipped)


def transpose2(matrix):
    """ Runtime: 64 ms, faster than 57.33% of Python3 online submissions for Transpose Matrix.
"""
    matrix2 = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix2[j][i] = matrix[i][j]
    return matrix2

def transpose3(matrix):
    """Runtime: 64 ms, faster than 57.33% of Python3 online submissions for Transpose Matrix.
"""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix = [[1, 2, 3], [3, 4, 5]]
print(transpose(matrix))
print(transpose2(matrix))
print(transpose3(matrix))