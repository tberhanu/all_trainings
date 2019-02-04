import unittest
import reverse_link_38 as foo

class TestReverseLink(unittest.TestCase):
    def test_iterative_reversing(self):
        solution = foo.Solution()
        lstnode1 = foo.ListNode(1)
        lstnode1.next = foo.ListNode(2)
        lstnode1.next.next = foo.ListNode(3)
        lstnode1.next.next.next = foo.ListNode(4)
        lstnode1.next.next.next.next = foo.ListNode(5)
        reversed_lst = solution.iteratively_reverseList(lstnode1)
        self.assertEqual(reversed_lst.val, 5)
        self.assertEqual(reversed_lst.next.val, 4)
        self.assertEqual(reversed_lst.next.next.val, 3)
        self.assertEqual(reversed_lst.next.next.next.val, 2)
        self.assertEqual(reversed_lst.next.next.next.next.val, 1)

    def test_recursive_reversing(self):
        solution = foo.Solution()
        lstnode1 = foo.ListNode(10)
        lstnode1.next = foo.ListNode(20)
        lstnode1.next.next = foo.ListNode(30)
        lstnode1.next.next.next = foo.ListNode(40)
        lstnode1.next.next.next.next = foo.ListNode(50)
        reversed_lst = solution.recursively_reverseList(lstnode1)
        self.assertEqual(reversed_lst.val, 50)
        self.assertEqual(reversed_lst.next.val, 40)
        self.assertEqual(reversed_lst.next.next.val, 30)
        self.assertEqual(reversed_lst.next.next.next.val, 20)
        self.assertEqual(reversed_lst.next.next.next.next.val, 10)


if __name__ == "__main__":
    unittest.main()