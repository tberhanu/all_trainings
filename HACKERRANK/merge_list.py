"""https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen"""
class SinglyLinkedList:
    pass
def mergeLists(head1, head2):
    node = SinglyLinkedList()
    node.data = -999
    dummy = node
    while head1 and head2:
        if head1.data <= head2.data:
            n = SinglyLinkedList()
            n.data = head1.data
            node.next = n
            head1 = head1.next
        else:
            n = SinglyLinkedList()
            n.data = head2.data
            node.next = n
            head2 = head2.next
        node = node.next
    if head1:
        node.next = head1
    if head2:
        node.next = head2

    return dummy.next
