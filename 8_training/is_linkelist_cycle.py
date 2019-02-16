"""
Runtime: 44 ms, faster than 94.54% of Python online submissions for Linked List Cycle.

"""


def hasCycle(head):
    """
    Runtime: 44 ms, faster than 94.54% of Python online submissions for Linked List Cycle.

    The trick is having two pointers moving ptr1 one step and ptr2 two steps at a time so that they will
    intersect on the same node at one time which cofirms us that there is a CYCLE.
    """
    if head == None:
        return False
    if head == head.next:
        return True
    ptr1 = head
    ptr2 = head.next
    while ptr1 != ptr2:

        if ptr2 == None or ptr2.next == None:
            return False
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next
    return True
