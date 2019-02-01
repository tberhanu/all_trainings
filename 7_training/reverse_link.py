""" 206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
Reverse a singly linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def iteratively_reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = None
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
        return tail
    def recursively_reverseList(self, head):
        tail = None
        hea = ListNode(head.val)
        hea.next = head.next
        def foo(tail, hea):
            if hea.next is not None:
                hea.next, hea, tail = tail, hea.next, hea
                return foo(tail, hea)
            else:
                hea.next = tail
                return hea
        return foo(tail, hea)

# print("*** The original Linked List nodes ****")
# lstnode1 = ListNode(1)
# lstnode1.next = ListNode(2)
# lstnode1.next.next = ListNode(3)
# lstnode1.next.next.next = ListNode(4)
# lstnode1.next.next.next.next = ListNode(5)
# for i in range(5):
#     print(lstnode1.val)
#     lstnode1 = lstnode1.next
# print("****** After reversing the Listnode: **********")
# solution = Solution()
# lstnode1 = ListNode(1)
# lstnode1.next = ListNode(2)
# lstnode1.next.next = ListNode(3)
# lstnode1.next.next.next = ListNode(4)
# lstnode1.next.next.next.next = ListNode(5)
# reversed_lst = solution.iteratively_reverseList(lstnode1)
# for i in range(5):
#     print(reversed_lst.val)
#     reversed_lst = reversed_lst.next
# print("****** Recursively reversing ******")
# solution = Solution()
# lstnode1 = ListNode(10)
# lstnode1.next = ListNode(20)
# lstnode1.next.next = ListNode(30)
# lstnode1.next.next.next = ListNode(40)
# lstnode1.next.next.next.next = ListNode(50)
# reversed_lst = solution.recursively_reverseList(lstnode1)
# for i in range(5):
#     print(reversed_lst.val)
#     reversed_lst = reversed_lst.next