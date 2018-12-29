#!/usr/bin/env python3.7

def input(n):
    try :
        assert (n in range(-5, 6)), "The input is out of the expected range"
        return True
    except AssertionError as e:
        return e

if __name__ == "__main__":

    for i in range(-7, 8):
        print(input(i))