"""
38. Reverse singly linked list i) Recursively ii) Iteratively
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    """
    :type head: ListNode

    """

    def iteratively_reverseList(self, head):
        tail = None
        while head:
            save = head.next
            head.next = tail
            tail = head
            head = save
        return tail


    def recursively_reverseList(self, head):
        tail = None
        def foo(head, tail):
            if head is None:
                return tail
            else:
                save = head.next
                head.next = tail
                tail = head
                head = save
                return foo(head, tail)
        return foo(head, tail)

