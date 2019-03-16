"""
https://www.hackerrank.com/challenges/compare-two-linked-lists/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""
def compare_lists(llist1, llist2):
    while llist1 and llist2:
        if llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next

    if llist1 is None and llist2 is None:
        return 1
    return 0
