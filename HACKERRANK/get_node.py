"""https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen"""
def getNode(head, positionFromTail):
    ptr1 = head
    ptr2 = head

    for _ in range(positionFromTail + 1):
        ptr1 = ptr1.next
    while ptr1:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr2.data