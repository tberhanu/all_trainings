#!/usr/bin/env python3
def decode_matrix(matrix):
    """decode_matrix(matrix) --> a function reading a matrix column wise which means read the first column and then
    continue to the second column, and also decode it by substituting any symbol/symbols found between the
    alphaneumeral will be substituted by a single space. Therefore, any symbol only comes before or after the
    alphaneumeral will stay there.

    ---> I followed the rule of NOT USING "IF", but still I would like comments and suggestions if there is a better
    and recommended way to do it.

    :param matrix: Double Array of Characters
    :return: String
    """
    s = ""
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            s = s + matrix[j][i]
    print("Original read string: {}".format(s))
    without_esp_chars = s.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    without_end_space = without_esp_chars.rstrip()
    without_front_space = without_esp_chars.lstrip()
    diff = len(without_esp_chars) - len(without_front_space)
    end_chars = s[len(without_end_space):]
    front_chars = s[:diff]


    return front_chars + ' '.join(without_esp_chars.split()) + end_chars

if __name__ == "__main__":
    print("Test 1: ")
    matrix = [["T", "s", "i"],
              ["h", "%", "x"],
              ["i", " ", "#"],
              ["s", "M", " "],
              ["$", "a", " "],
              ["#", "t", "%"],
              ["i", "r", "!"]]
    statement = decode_matrix(matrix)
    print("Decoded String      : {}".format(statement))
    print("Test2: ")
    matrix = [["%", "s", "o"],
              ["@", "o", "k"],
              ["h", "%", "*"],
              ["e", " ", "#"],
              ["y", "m", " "],
              ["$", "e", " "],
              ["#", "a", "%"],
              ["a", "n", "o"],
              ["l", " ", "k"]]
    statement = decode_matrix(matrix)
    print("Decoded String      : {}".format(statement))
    print("Test 3: ")
    matrix = [["%", "s", "o"],
              ["T", "o", "k"],
              ["h", "%", "*"],
              ["e", " ", "#"],
              ["y", "m", " "],
              ["$", "e", " "],
              ["#", "a", "%"],
              ["a", "n", ")"],
              ["l", " ", "="]]
    statement = decode_matrix(matrix)
    print("Decoded String      : {}".format(statement))
