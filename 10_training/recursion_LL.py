class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

def swap_adjacents_value(head):
    dummy = LinkedList(-9)
    dummy.next = head
    swap(head)
    return dummy

def swap(head):
    if head is None or head.next is None:
        return
    save = head.next
    head.next = head.next.next
    save.next = head
    swap(head.next.next)

head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(5)

res = swap_adjacents_value(head)
while res:
    print(res.val)
    res = res.next

