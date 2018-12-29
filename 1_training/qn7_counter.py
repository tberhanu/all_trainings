#!/usr/bin/env python3.7

def count_pattern(str):
    """count_pattern(str) --> counts the number of a's followed by 0 within the string

    :param str: String
    :return: integer
    """
    cntr = 0
    for i in range(len(str) - 1):
        if str[i] + str[i + 1] == "a0":
            cntr = cntr + 1
    return cntr

if __name__ == "__main__":

    print(count_pattern("a0kkka0hdhda0"))
    print(count_pattern("kida0 a 0 defa00a"))