#!/usr/bin/env python3

def inplace_reverse(msg):
    """inplace_reverse(msg) --> a function receiving an array of characters forming a word separated by a single space,
    and output after revering the words, not switching the characters, inplace.

    :param msg: Array of Characters
    :return: Array of Characters
    """

    msg.reverse()
    start = 0
    end = 0
    for m in msg:
        if m == ' ':
            reversing(msg, start, end - 1)
            start = end + 1
            end = end + 1
        elif end == len(msg) - 1:
            reversing(msg, start, end)
        else:
            end = end + 1

def reversing(msg, start, end):
    while start < end:
        swap(msg, start, end)
        start = start + 1
        end = end - 1

def swap(msg, start, end):
    temp = msg[start]
    msg[start] = msg[end]
    msg[end] = temp




if __name__ == "__main__":

    msg = ['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']
    inplace_reverse(msg)
    print(''.join(msg))
    msg2 = ['h', 'e', 'l', 'l', 'o', ' ', 'a', 'l', 'l', ' ', 'n', 'e', 'w', ' ', 'w', 'o', 'r', 'l', 'd']
    inplace_reverse(msg2)
    print(''.join(msg2))
