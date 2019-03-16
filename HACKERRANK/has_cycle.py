def has_cycle(head):
    if head is None:
        return 0
    ptr = head
    while True:
        if head.next is None or head.next.next is None:
            return 0

        head = head.next.next
        ptr = ptr.next
        if head == ptr:
            return 1