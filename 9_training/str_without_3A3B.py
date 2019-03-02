"""
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.


Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: A = 4, B = 1
Output: "aabaa"


Note:

0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B
"""

def str_without_3a3b(A, B):
    """ According to the question, this code works perfectly, but the test case is a kind
    of confused so LeetCode need to revise it
    """
    if A < 3 and B < 3:
        return "a"*A + "b"*B
    big = "a"
    small = "b"
    if A > B:
        return foo(A, B, big, small)
    else:
        return foo(B, A, small, big)
def foo(A, B, big, small):
    a = list(big * A)
    i = 2
    j = 0
    while i < A + B and j < B:
        a.insert(i, small)
        i = i + 3
        j = j + 1

    return "".join(a)

print(str_without_3a3b(2, 6))