""" https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None



def addTwoNumbers(l1, l2):

    ll = LinkedList(999)
    root = ll
    carry = 0
    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        sum = val1 + val2 + carry
        remainder = sum % 10
        carry = sum // 10
        ll.next = LinkedList(remainder)
        ll = ll.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    if carry > 0:
        ll.next = LinkedList(carry)
    return root.next


ll1 = LinkedList(2)
ll1.next = LinkedList(4)
ll1.next.next = LinkedList(3)
l1 = LinkedList(5)
l1.next = LinkedList(6)
l1.next.next = LinkedList(4)
ll = addTwoNumbers(ll1, l1)

while ll:
    print(ll.val)
    ll = ll.next
