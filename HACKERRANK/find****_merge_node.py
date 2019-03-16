"""
https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists&h_r=next-challenge&h_v=zen
"""
class SinglyLinkedListNode:
    pass

def findMergeNode(headA, headB):
    """
    Once the shorted pointer reaches the end, and start from the root of the longer
    node, the longer also did the same thing but in reverse order like after reaching
    the end, it will start over from the root of the shorter node. Therefore, both ways,
    they step equal number of steps, and eventually will arrive the COMMON INTERSECTION NODE.
    step m + n = step n + m

    *** This concept reminds me how to check if the link is CYCLIC somewhere or not where we
    had two pointers--one steps single step and other steps double steps. If both pointers meet
    at the same node, then it's CYCLIC. If one pointer reaches the END, then it's not CYCLIC.

    """
    currentB = headB
    currentA = headA

    # Do till the two nodes are the same
    while (currentA != currentB):
        # If you reached the end of one list start at the beginning of the other one
        # currentA
        if (currentA.next == None):
            currentA = headB
        else:
            currentA = currentA.next

        # currentB
        if (currentB.next == None):
            currentB = headA
        else:
            currentB = currentB.next

    return currentB.data
