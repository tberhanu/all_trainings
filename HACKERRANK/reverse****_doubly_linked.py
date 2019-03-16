"""https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists"""
def reverse_doubly_linked(head):
    """ Passed all the tests.

    """
    prev = head.prev
    next = head.next
    while head:
        head.prev = next
        head.next = prev
        prev = head
        head = next
        if next:
            next = next.next


    return prev
