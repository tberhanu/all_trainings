
class LL:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def rotate(head, n):
    dummy = head
    p1 = head
    p2 = head
    for i in range(n-1):
        p1 = p1.next
    while p1.next:
        p1 = p1.next
        p2 = p2.next

    ans = p2.next
    p2.next = None

    p1.next = dummy

    return ans

# 1->2->3->4->5->None, 2 => 4->5->1->2->3->NULL
root = LL(1, LL(2, LL(3, LL(4, LL(5)))))
ll = rotate(root, 3)
while ll:
    print(ll.val)
    ll = ll.next