"""https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen"""
def removeDuplicates(head):
    if head is None:
        return None
    dummy = head
    p1 = head
    p2 = head.next
    while p2:
        if p1.data == p2.data:
            p2 = p2.next
            p1.next = p1.next.next
        else:
            p1 = p1.next
            p2 = p2.next
    return dummy