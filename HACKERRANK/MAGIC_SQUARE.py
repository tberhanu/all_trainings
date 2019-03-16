
"""
https://www.hackerrank.com/challenges/magic-square-forming/problem

Take Away: How to deal with two matrices element by element using double for loop,
    and ofcourse triple for loop to compare a single matrix with other multiple matrices"""
class Magic:

    matrices = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]

    def evaluate(self, matrix):
        totals = []
        for mat in self.matrices:
            total = 0
            for mat_row, matrix_row in zip(mat, matrix):
                for i, j in zip(mat_row, matrix_row):
                    if not i == j:
                        total += abs(i - j)
            totals.append(total)
        return min(totals)


matrix = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

magic = Magic()
print(magic.evaluate(matrix))

