#!/usr/bin/env python3

def condense_meeting(arr):
    """condense_meeting(arr) --> a function that takes an array of tuples to represent the beginning and end of the
    meeting, and gives the condensed form of all the occupied timings for meeting

    :param arr: Array of tuples
    :return: Array of tuples
    """

    sorted_arr = sorted(arr, key=lambda tup: tup[0])
    i = len(arr) - 1
    while i - 1 >= 0:
        if sorted_arr[i - 1][1] >= sorted_arr[i][0]:
            start = sorted_arr[i - 1][0]
            end = max(sorted_arr[i - 1][1], sorted_arr[i][1])
            tup = (start, end)
            del sorted_arr[i]
            del sorted_arr[i - 1]
            sorted_arr.append(tup)
            sorted_arr = sorted(sorted_arr, key=lambda tup: tup[0])

        i = i - 1
    return sorted_arr

if __name__ == "__main__":
    print(condense_meeting([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
    print(condense_meeting([(0, 6), (6, 7), (4, 8), (10, 12), (9, 12)]))


