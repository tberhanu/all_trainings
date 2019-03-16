"""
https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem?h_r=next-challenge&h_v=zen
"""
def reversePrint(head):
    if head.next:
        reversePrint(head.next)
    print(head.data)


    