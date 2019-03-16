"""https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists&isFullScreen=true"""
class SinglyLinkedListNode:
    pass
def insertNodeAtPosition(head, data, position):
    dummy = head

    for _ in range(position - 1):
        head = head.next
    if head.next:
        temp = head.next
        head.next = SinglyLinkedListNode(data)
        head.next.next = temp

    return dummy
