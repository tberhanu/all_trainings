"""Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    """Runtime: 40 ms, faster than 37.95% of Python3 online submissions for Swap Nodes in Pairs.

    THIS QUESTION IS TRICKY TRICKY, SO just become more TRICKIER AND TRICKIER.

    Take Away: When dealing with such tricky LINKED LIST questions, draw the nodes, and mark the arrows
            step by step like 'step1' for the first action, 'step2' for the second action, .......
            Then following it, code BRAVELY exactly what you see on your DIAGRAM.
"""
    prev = head
    dummy = head.next
    i = 0
    while head and head.next:

        temp = head.next
        head.next = head.next.next
        temp.next = head
        if i == 1:
            prev.next = temp
            prev = head
        head = head.next

        i = 1

    return dummy

