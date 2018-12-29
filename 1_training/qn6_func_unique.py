#!/usr/bin/env python3.7


from collections import Counter
def func_unique(str):
    """func_unique(str) --> Returns True if all the letters are unique, and return  False otherwise

    :param str: String
    :return: Boolean
    """
    counter = Counter(str)
    return not any([v for v in counter.values() if v > 1])

if __name__ == "__main__":

    # print(func_unique.__doc__)
    print(func_unique("hello"))
    print(func_unique("helo"))
    print(func_unique("abd kfg dip"))