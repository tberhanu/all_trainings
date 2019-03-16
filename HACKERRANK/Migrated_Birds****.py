"""https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=next-challenge&h_v=zen&isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen"""

"""  WATCH OUT WATCH OUT FOR SOME SILLY QUESTIONS NOT TO WASTE YOUR TIME

 *** This question is basically to get the most common number out of the array, with
 one corner case added, i.e. if more than one number with the same highest frequency, then 
 take the SMALLEST ONE.
 
 HOPE THERE WILL BE A BETTER SOLUTION.
"""
def migratoryBirds(arr):
    from collections import Counter
    freq = Counter(arr)
    commons = freq.most_common(len(arr))
    e = commons[0][0]
    val = commons[0][1]
    for tup in commons:
        if tup[1] != val:
            return e
        if tup[1] == val and e < tup[0]:
            return e
        if tup[1] == val and tup[0] < e:
            e = tup[0]

    return e



migratoryBirds([1, 1, 2, 2, 3, 2, 1])