"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def is_palindrome(head):
    """Runtime: 76 ms, faster than 78.65% of Python3 online submissions for Palindrome Linked List.
"""
    start1 = head
    runner1 = head
    runner2 = head
    while runner2 and runner2.next:
        runner1 = runner1.next
        runner2 = runner2.next.next

    start2 = runner1.next if runner2 and runner2.next is None else runner1

    arr1, arr2 = [], []
    while start2:
        arr1.append(start1.val)
        arr2.append(start2.val)
        start1 = start1.next
        start2 = start2.next

    return arr1 == arr2[::-1]

head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
print(is_palindrome(head))