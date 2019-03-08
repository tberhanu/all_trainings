"""Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    """Runtime: 44 ms, faster than 49.47% of Python3 online submissions for Remove Nth Node From End of List.

    This Qn should be easy, but watch out the EDGE CASES.
"""
    if head.next is None:
        return None
    dummy = head
    ptr = head
    i = 0
    for _ in range(n):
        head = head.next
        i = i + 1

    if head is None and i == n:
        return dummy.next
    while head and head.next:
        ptr = ptr.next
        head = head.next

    ptr.next = ptr.next.next

    return dummy
