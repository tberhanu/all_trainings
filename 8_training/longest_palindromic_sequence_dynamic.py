""" FAILED SOME OF THE TESTS"""
def longest_palindrome_dynamic_programming(string):
    """ The abstract meaning of the matrix is: Starting from index called row
    up to index called col with respect to the string, not matrix.
    """
    if string == "":
        return string
    pal = string[0]
    matrix = [[False]*len(string) for _ in range(len(string))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == col:
                matrix[row][col] = True
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            matrix[i][i+1] = True
            pal = string[i:i+2]
    for row in range(len(matrix)):
        for col in range(row+1, len(matrix[0])):
            if string[row] == string[col] and matrix[row+1][col-1]:
                matrix[row][col] = True
                if len(string[row:col+1]) > len(pal):
                    pal = string[row:col+1]

    return pal




def get_length(string):
    if string == string[::-1]:
        return len(string)
    else:
        return max(get_length(string[1:]), get_length(string[:-1]))


print(longest_palindrome_dynamic_programming('eabcb'), get_length('eabcb'))
print(longest_palindrome_dynamic_programming("babad"), get_length('babad'))
print(longest_palindrome_dynamic_programming("b"), get_length('b'))
print(longest_palindrome_dynamic_programming("baabaabk"), get_length("baabaabk"))
print(longest_palindrome_dynamic_programming("baab"), get_length("baab"))
print(longest_palindrome_dynamic_programming("abcdefg"), get_length("abdefg"))
print(longest_palindrome_dynamic_programming("bananas"), get_length("bananas"))
