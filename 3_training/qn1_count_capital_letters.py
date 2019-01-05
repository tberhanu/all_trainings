#!/usr/bin/env python3
def count_capital_letters(file):
    """

    :param file: A file within the same directory with this code
    :return: integer
    """
    cntr = 0
    last = ""
    with open(file, 'r') as rf:
        for line in rf:
            for ch in line:
                if ch.isupper():
                    cntr = cntr + 1
        return cntr


if __name__ == "__main__":
    count = count_capital_letters("file.txt")
    print(count)

