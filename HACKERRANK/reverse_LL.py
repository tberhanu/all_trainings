"""
https://www.hackerrank.com/challenges/reverse-a-linked-list/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""
def reverse(head):
    if head is None or head.next is None:
        return head
    p = None

    while head:
        save = head.next
        head.next = p
        p = head
        head = save
        if save:
            save = save.next
    return p

