"""
https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
This code passes most of the tests, but failed to run as fast as expected with some of the hackerrank tests.
"""
def commonChild_dynamic(s1, s2):
    col = len(s2) + 1
    row = len(s1) + 1
    matrix =[[0] * col for _ in range(row)]
    return LCS_dynamic(s1, s2, matrix)


def LCS_dynamic(s1, s2, matrix):
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if s2[i - 1] == s1[j - 1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])

            # if matrix[i][j] > highest:
            #     highest = matrix[i][j]
    return matrix[len(s1)][len(s2)]
    # return highest


def commonChild_recursive(str1, str2):

    i, j = 0, 0
    return LCS_recursive(str1, i, str2, j)


def LCS_recursive(str1, i, str2, j):
    if i == len(str1) or j == len(str2):
        return 0
    elif str1[i] == str2[j]:
        return 1 + LCS_recursive(str1, i + 1, str2, j + 1)
    else:
        return max(LCS_recursive(str1, i + 1, str2, j), LCS_recursive(str1, i, str2, j + 1))

s1 = "abcd"
s2 = "abdc"
print(commonChild_dynamic(s1, s2))
print(commonChild_recursive(s1, s2))
print("-------------------")
s1 = "harry"
s2 = "sally"
print(commonChild_dynamic(s1, s2))
print(commonChild_recursive(s1, s2))

print("-------------------")
s1 = "aa"
s2 = "bb"
print(commonChild_dynamic(s1, s2))
print(commonChild_recursive(s1, s2))

print("-------------------")
s1 = "SHINCHAN"
s2 = "NOHARAAA"
print(commonChild_dynamic(s1, s2))
print(commonChild_recursive(s1, s2))

print("-------------------")
s1 = "ABCDEF"
s2 = "FBDAMN"
print(commonChild_dynamic(s1, s2))
print(commonChild_recursive(s1, s2))

print("-------------------")
s1 = "OUDFRMYMAW"
s2 = "AWHYFCCMQX"
print(commonChild_dynamic(s1, s2))
print(commonChild_recursive(s1, s2))

#Expected 2