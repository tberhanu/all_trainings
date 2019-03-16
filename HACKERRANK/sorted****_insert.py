
"""https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists&isFullScreen=true&h_r=next-challenge&h_v=zen"""
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
class DoublyLinkedListNode():
    pass


def sortedInsert(head, data):
    dummy = head
    prev = head
    if head.data >= data:
        node = DoublyLinkedListNode(data)
        node.next = head
        head.prev = node
        return node

    while head and head.data < data:
        prev = head
        head = head.next

    if head is None:
        node = DoublyLinkedListNode(data)
        prev.next = node
        node.prev = prev
    else:
        node = DoublyLinkedListNode(data)
        prev.next = node
        node.prev = prev

        node.next = head
        head.prev = node

    return dummy