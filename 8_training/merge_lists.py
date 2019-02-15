"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    ll = ListNode(999)
    root = ll
    while l1 and l2:
        if l1.val <= l2.val:
            ll.next = ListNode(l1.val)
            ll = ll.next
            l1 = l1.next
        elif l2.val < l1.val:
            ll.next = ListNode(l2.val)
            ll = ll.next
            l2 = l2.next

    if l1:
        ll.next = l1
    elif l2:
        ll.next = l2

    return root.next


l1 = ListNode(99)
l2 = ListNode(99)
root1 = l1
root2 = l2
for a in [1,2,4]:
    l1.next = ListNode(a)
    l1 = l1.next

for b in [1,3,4]:
    l2.next = ListNode(b)
    l2 = l2.next
r1 = root1.next
r2 = root2.next

ll = mergeTwoLists(r1, r2)
while ll:
    print(ll.val)
    ll = ll.next
