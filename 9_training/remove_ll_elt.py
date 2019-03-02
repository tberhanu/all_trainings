"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_element(head, val):
    """ The take away is you need this dummy nod badly """
    dummy = ListNode(-1)
    dummy.next = head
    ptr = dummy

    while ptr and ptr.next:
        if ptr.next.val == val:
            ptr.next = ptr.next.next
        else:
            ptr = ptr.next
    return dummy.next

