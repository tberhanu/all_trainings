"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_duplicates(head):
    root = head
    while head:
        if head.next and head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return root


head = ListNode(999)
root = head
for i in range(10):
    head.next = ListNode(i)
    head.next = ListNode(i)
    head = head.next

while root.next:
    print(root.next.val)
    root = root.next
